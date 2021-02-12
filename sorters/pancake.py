#!/usr/bin/python3

from sorters.sort_base import sort_base
from sort_util.data_tools import data_store


class pancake_sort(sort_base):
    def __init__(self) -> None:
        super().__init__()

    def name(self) -> str:
        return 'Pancake'

    def _do_sort(self, data: data_store) -> None:
        curr_size = data.size()
        while curr_size > 1:
            max_index = self.__find_max(data, curr_size)
            if max_index != curr_size - 1:
                self.__flip(data, max_index)
                self.__flip(data, curr_size - 1)
            curr_size -= 1

    def __flip(self, data: data_store, end: int) -> None:
        start = 0
        while start < end:
            data.swap(start, end)
            start += 1
            end -= 1

    def __find_max(self, data: data_store, size: int) -> int:
        max_index = 0
        for i in range(0, size):
            if data.is_greater_than(i, max_index):
                max_index = i
        return max_index
