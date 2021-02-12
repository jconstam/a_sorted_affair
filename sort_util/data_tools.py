#!/usr/bin/python3

import os
import datetime
import subprocess

import cv2

from sort_util.image_tools import draw_image


class data_store:
    def __init__(self, drawer: draw_image, video: cv2.VideoWriter) -> None:
        self.__data = None
        self.__drawer = drawer
        self.__video = video
        self.__name = ''
        self.__frame_counter = 0
        self.__ticker = 0
        self.__frame_frequency = 1
        self.__reset_stats()

    def __reset_stats(self) -> None:
        self.accesses = 0
        self.swaps = 0
        self.compares = 0
        self.moves = 0

    def __str__(self) -> str:
        return '{}'.format(self.__data)

    def __check_loaded(self) -> None:
        assert self.__data, 'must load data before accessing'

    def size(self) -> int:
        self.__check_loaded()
        return len(self.__data)

    def max(self) -> int:
        self.__check_loaded()
        return max(self.__data)

    def sortedness(self) -> float:
        sum = 0
        bin_size = min(10, len(self.__data))
        count = len(self.__data) - bin_size
        for i in range(count):
            for j in range(i + 1, i + bin_size):
                if self.__data[j] >= self.__data[i]:
                    sum += 1
        sortedness = (((sum / ((bin_size - 1) * count)) * 100) - 50) * 2
        return sortedness if sortedness > 0.0 else 0.0

    def load(self, data: list, name: str) -> None:
        for value in data:
            assert type(value) is int, 'data must contain only ints'
        self.__data = data
        self.__reset_stats()
        self.draw(name)

    def __getitem__(self, key: int) -> int:
        self.__check_loaded()
        self.accesses += 1
        return self.__data[key]

    def __setitem__(self, key: int, value: int) -> None:
        self.__check_loaded()
        self.accesses += 1
        self.__data[key] = value
        self.draw()

    def init(self, name: str, frame_freq: int) -> None:
        self.__name = name
        self.__frame_frequency = frame_freq

    def draw(self, force: bool = False) -> None:
        if not force:
            self.__ticker += 1
            if self.__ticker % self.__frame_frequency != 0:
                return

        self.__frame_counter += 1
        if self.__drawer and self.__video:
            self.__video.write(self.__drawer.draw(self, self.__name))

    def convert(self, in_file: str, out_file: str) -> None:
        if os.path.exists(out_file):
            os.remove(out_file)
        print('Converting {} to {}'.format(in_file, out_file))
        start = datetime.datetime.now()
        process = subprocess.Popen(
            ['ffmpeg', '-i', in_file, out_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        process.wait()
        end = datetime.datetime.now()
        print('\tDone in {}'.format(end - start))
        os.remove(in_file)

    def swap(self, index1: int, index2: int, skip_draw=False) -> None:
        self.__check_loaded()
        self.__data[index1], self.__data[index2] = self.__data[index2], self.__data[index1]
        self.swaps += 1
        self.draw()

    def move(self, index_source: int, index_dest: int) -> None:
        self.__check_loaded()
        temp = self.__data[index_source]
        del self.__data[index_source]
        self.__data.insert(index_dest, temp)
        self.moves += 1
        self.draw()

    def is_equal_to(self, index1: int, index2: int) -> bool:
        self.__check_loaded()
        self.compares += 1
        return self.__data[index1] == self.__data[index2]

    def is_less_than(self, index1: int, index2: int) -> bool:
        self.__check_loaded()
        self.compares += 1
        return self.__data[index1] < self.__data[index2]

    def is_greater_than(self, index1: int, index2: int) -> bool:
        self.__check_loaded()
        self.compares += 1
        return self.__data[index1] > self.__data[index2]

    def is_greater_than_or_equal(self, index1: int, index2: int) -> bool:
        self.__check_loaded()
        self.compares += 1
        return self.__data[index1] >= self.__data[index2]
