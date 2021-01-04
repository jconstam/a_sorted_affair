#!/usr/bin/python3

from sorters.sort_base import sort_base
from sort_video.data_tools import data_store


class insertion_sort(sort_base):
    def __init__(self) -> None:
        super().__init__()

    def name(self) -> str:
        return 'Insertion'

    def _do_sort(self, data: data_store) -> None:
        for i in range(1, data.size()):
            src_index = i
            for j in range(0, i):
                if data.is_greater_than(src_index, j):
                    data.move(src_index, j)
                    break
            data.draw()
