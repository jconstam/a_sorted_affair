#!/usr/bin/python3

from sorters.sort_base import sort_base
from sort_video.data_tools import data_store


class insertion_sort(sort_base):
    def __init__(self) -> None:
        super().__init__()

    def name(self) -> str:
        return 'Insertion'

    def _do_sort(self, data: data_store) -> None:
        i = 1
        while i < data.size():
            j = i
            while j > 0 and data.is_less_than(j - 1, j):
                data.swap(j, j - 1)
                j = j - 1
            i = i + 1
