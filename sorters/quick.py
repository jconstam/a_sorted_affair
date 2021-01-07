#!/usr/bin/python3

import random

from sorters.sort_base import sort_base
from sort_util.data_tools import data_store


class quick_sort(sort_base):
    def __init__(self) -> None:
        super().__init__()
        self.draw_counter = 0

    def name(self) -> str:
        return 'Quick'

    def _do_sort(self, data: data_store) -> None:
        self.__quick_sort(data, 0, data.size() - 1)

    def __quick_sort(self, data: data_store, low: int, high: int) -> None:
        if low < high:
            pivot = self.__partition(data, low, high)

            self.__quick_sort(data, low, pivot - 1)
            self.__quick_sort(data, pivot + 1, high)

    def __partition(self, data: data_store, low: int, high: int) -> None:
        pivot_index = random.randint(low, high)
        data.swap(pivot_index, low)
        pivot_index = low

        for j in range(low + 1, high + 1):
            if data.is_less_than(j, pivot_index):
                data.move(j, pivot_index)
                pivot_index += 1

                self.draw_counter += 1
                if self.draw_counter % 10 == 0:
                    data.draw(self.name())
        data.draw(self.name())
        return pivot_index
