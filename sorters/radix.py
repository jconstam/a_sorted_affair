#!/usr/bin/python3

from sorters.sort_base import sort_base
from sort_util.data_tools import data_store


class radix_sort(sort_base):
    def __init__(self) -> None:
        super().__init__()
        self.draw_counter = 0

    def name(self) -> str:
        return 'Radix'

    def _do_sort(self, data: data_store) -> None:
        max = data.max()

        exp = 1
        while max / exp > 0:
            self.radix_sort(data, exp)
            exp *= 10

    def radix_sort(self, data: data_store, exp: int) -> None:
        n = data.size()

        count = [0] * 10
        for i in range(0, data.size()):
            count[int(data[i] / exp) % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(data.size() - 1, 0, -1):
            curr = data[i]
            idx = int(curr / exp) % 10
            data.swap(count[idx] - 1, i)
            count[idx % 10] -= 1

            self.draw_counter += 1
            if self.draw_counter % 100 == 0:
                data.draw(self.name())