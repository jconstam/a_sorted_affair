#!/usr/bin/python3

from sorters.sort_base import sort_base
from sort_util.data_tools import data_store


class bubble_sort(sort_base):
    def __init__(self) -> None:
        super().__init__()

    def name(self) -> str:
        return 'Bubble'

    def frame_frequency(self) -> int:
        return 500

    def _do_sort(self, data: data_store) -> None:
        sorted = False
        while not sorted:
            sorted = True
            for i in range(data.size() - 1):
                if data.is_greater_than(i, i + 1):
                    data.swap(i, i + 1, skip_draw=True)
                    sorted = False
