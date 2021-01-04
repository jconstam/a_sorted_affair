#!/usr/bin/python3

import os

from sort_video import image_tools

class data_store:
    def __init__(self, drawer: image_tools.draw_image, file_name: str) -> None:
        self.__data = None
        self.__drawer = drawer
        self.__file_name = file_name
        self.__file_index = 0
        self.__reset_stats()

    def __reset_stats(self) -> None:
        self.__accesses = 0
        self.__swaps = 0

    def __current_file_name(self) -> str:
        name, ext = os.path.splitext(self.__file_name)
        curr_name = '{}_{}{}'.format(name, self.__file_index, ext)
        self.__file_index = self.__file_index + 1
        return curr_name

    def __update_stats(self, draw=False, swap=False, access=False) -> None:
        if swap:
            self.__swaps = self.__swaps + 1
            draw = True
        if access:
            self.__accesses = self.__accesses + 1

        if draw:
            self.__drawer.draw(self.__data, self.__current_file_name())

    def load(self, data: list) -> None:
        for value in data:
            assert type(value) is int, 'data must contain only ints'
        self.__data = data
        self.__reset_stats()
        self.__update_stats(draw=True)

    def __getitem__(self, key: int) -> int:
        assert self.__data, 'must load data before accessing'
        self.__update_stats(access=True)
        return self.__data[key]

    def swap(self, index1: int, index2: int) -> None:
        assert self.__data, 'must load data before accessing'
        temp = self.__data[index1]
        self.__data[index1] = self.__data[index2]
        self.__data[index2] = temp
        self.__update_stats(swap=True)
