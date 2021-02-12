#!/usr/bin/python3

from sorters.sort_base import sort_base
from sort_util.data_tools import data_store


class comb_sort(sort_base):
    def __init__(self) -> None:
        super().__init__()

    def name(self) -> str:
        return 'Comb'

    def frame_frequency(self) -> int:
        return 13

    def _do_sort(self, data: data_store) -> None:
        size = data.size()
        gap = size
        swapped = True
        while gap != 1 or swapped:
            gap = self.get_next_gap(gap)
            swapped = False
            for i in range(0, size - gap):
                if data[i] > data[i + gap]:
                    data.swap(i, i + gap)
                    swapped = True

    def get_next_gap(self, gap):
        gap = int((gap * 10) / 13)
        return gap if gap > 1 else 1
