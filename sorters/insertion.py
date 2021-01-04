#!/usr/bin/python3

from sorters import sort_base
from sort_video import data_tools


class insertion(sort_base.sort_base):
    def __init__(self) -> None:
        super().__init__()

    def _sort_name(self) -> str:
        return 'Insertion'

    def _do_sort(self, data: data_tools.data_store) -> None:
        sorted = False
        while not sorted:
            sorted = True
            for index in range(data.size() - 1):
                if data.is_less_than(index, index + 1):
                    data.swap(index, index + 1)
                    sorted = False
