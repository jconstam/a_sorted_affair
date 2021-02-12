#!/usr/bin/python3

from sorters.sort_base import sort_base
from sort_util.data_tools import data_store


class gnome_sort(sort_base):
    def __init__(self) -> None:
        super().__init__()

    def name(self) -> str:
        return 'Gnome'

    def _do_sort(self, data: data_store) -> None:
        index = 0
        while index < data.size():
            if index == 0:
                index += 1
            elif data.is_greater_than_or_equal(index, index - 1):
                index += 1
            else:
                data.swap(index, index - 1)
                index -= 1
