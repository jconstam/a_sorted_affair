#!/usr/bin/python3

import math

from sorters.sort_base import sort_base
from sort_util.data_tools import data_store


class radix_sort(sort_base):
    def __init__(self) -> None:
        super().__init__()

    def name(self) -> str:
        return 'Radix'

    def frame_frequency(self) -> int:
        return 16900

    def _do_sort(self, data: data_store) -> None:
        max = data.max()
        exp = 1

        while int(max / exp) > 0:
            while self.radix_sort(data, exp):
                pass
            exp *= 10

    def is_greater_than(self, data: data_store, exp: int, idx1: int, idx2: int) -> bool:
        one = int(data[idx1] / exp) % 10
        two = int(data[idx2] / exp) % 10
        return one > two

    def radix_sort(self, data: data_store, exp: int) -> bool:
        changed = False
        for i in range(0, data.size() - 1):
            if self.is_greater_than(data, exp, i, i + 1):
                data.swap(i, i + 1)
                changed = True
        return changed
