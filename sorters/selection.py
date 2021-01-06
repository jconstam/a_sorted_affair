#!/usr/bin/python3

from sorters.sort_base import sort_base
from sort_video.data_tools import data_store


class selection_sort(sort_base):
    def __init__(self) -> None:
        super().__init__()

    def name(self) -> str:
        return 'Selection'

    def _do_sort(self, data: data_store) -> None:
        for i in range(data.size()):
            min_index = i
            for j in range(i + 1, data.size()):
                if data.is_greater_than(min_index, j):
                    min_index = j
            if not i == min_index:
                data.swap(min_index, i)
            data.draw(self.name())
