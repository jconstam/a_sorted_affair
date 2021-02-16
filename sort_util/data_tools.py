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

    def load(self, data: list) -> None:
        for value in data:
            assert type(value) is int, 'data must contain only ints'
        self.__data = data
        self.__reset_stats()
        self.draw()

    def __getitem__(self, key: int) -> int:
        self.__check_loaded()
        self.accesses += 1
        return self.__data[key]

    def __setitem__(self, key: int, value: int) -> None:
        self.set(key, value)

    def set(self, key: int, value: int, skip_draw: bool = False) -> None:
        self.__check_loaded()
        self.accesses += 1
        self.__data[key] = value
        if not skip_draw:
            self.draw()
        

    def init(self, name: str) -> None:
        self.__name = name

    def draw(self) -> None:
        self.__frame_counter += 1
        if self.__drawer and self.__video:
            self.__video.write(self.__drawer.draw(self, self.__name))

    def convert(self, in_file: str, out_file: str) -> None:
        if os.path.exists(out_file):
            os.remove(out_file)
        print('Converting {} to {}'.format(in_file, out_file))
        start = datetime.datetime.now()
        process = subprocess.Popen(['ffmpeg', '-i', in_file, out_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        process.wait()
        end = datetime.datetime.now()
        print('\tDone in {}'.format(end - start))
        os.remove(in_file)

    def adjust_length(self, file: str, target_len: float, fps: int) -> None:
        process = subprocess.Popen(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file],
                                   stdout=subprocess.PIPE)
        (length_bytes, _) = process.communicate()
        orig_len = float(length_bytes.decode('utf-8'))
        ratio = target_len / orig_len

        filename, file_extension = os.path.splitext(file)
        in_file = filename + '_old' + file_extension
        os.rename(file, in_file)

        print('Changing video length from {} to {} ({:.3f})'.format(orig_len, target_len, ratio))
        start = datetime.datetime.now()
        process = subprocess.Popen('ffmpeg -i {} -filter:v \"setpts={}*PTS\" {}'.format(in_file, ratio, file),
                                   shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        process.wait()
        end = datetime.datetime.now()
        print('\tDone in {}'.format(end - start))
        os.remove(in_file)

        in_file = filename + '_old' + file_extension
        os.rename(file, in_file)

        print('Smoothing/interpolating video')
        start = datetime.datetime.now()
        process = subprocess.Popen('ffmpeg -i {} -filter:v \"minterpolate=\'mi_mode=mci:mc_mode=aobmc:vsbmc=1:fps={}\'\" {}'.format(in_file, fps, file),
                                   shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        process.wait()
        end = datetime.datetime.now()
        print('\tDone in {}'.format(end - start))
        os.remove(in_file)

    def swap(self, index1: int, index2: int, skip_draw=False) -> None:
        self.__check_loaded()
        self.__data[index1], self.__data[index2] = self.__data[index2], self.__data[index1]
        self.swaps += 1
        if not skip_draw:
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
