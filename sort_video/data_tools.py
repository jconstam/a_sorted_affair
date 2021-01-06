#!/usr/bin/python3

import os
import datetime
import subprocess

import cv2

from sort_video.image_tools import draw_image

class data_store:
    def __init__(self, drawer: draw_image, video: cv2.VideoWriter) -> None:
        self.__data = None
        self.__drawer = drawer
        self.__video = video
        self.__reset_stats()

    def __reset_stats(self) -> None:
        self.accesses = 0
        self.swaps = 0
        self.compares = 0
        self.moves = 0

    def __check_loaded(self) -> None:
        assert self.__data, 'must load data before accessing'

    def size(self) -> int:
        self.__check_loaded()
        return len(self.__data)

    def load(self, data: list, name: str) -> None:
        for value in data:
            assert type(value) is int, 'data must contain only ints'
        self.__data = data
        self.__reset_stats()
        self.draw(name)

    def __getitem__(self, key: int) -> int:
        self.__check_loaded()
        self.accesses = self.accesses + 1
        return self.__data[key]

    def draw(self, name) -> None:
        self.__video.write(self.__drawer.draw(self, name))

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
        temp = self.__data[index1]
        self.__data[index1] = self.__data[index2]
        self.__data[index2] = temp
        self.swaps = self.swaps + 1

    def move(self, index_source: int, index_dest: int) -> None:
        self.__check_loaded()
        temp = self.__data[index_source]
        del self.__data[index_source]
        self.__data.insert(index_dest, temp)
        self.moves = self.moves + 1


    def is_less_than(self, index1: int, index2: int) -> bool:
        self.__check_loaded()
        self.compares = self.compares + 1
        return self.__data[index1] < self.__data[index2]

    def is_greater_than(self, index1: int, index2: int) -> bool:
        self.__check_loaded()
        self.compares = self.compares + 1
        return self.__data[index1] > self.__data[index2]

