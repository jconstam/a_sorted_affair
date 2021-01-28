#!/usr/bin/python3

from sorters.sort_base import sort_base
from sort_util.data_tools import data_store


class shell_sort(sort_base):
    def __init__(self) -> None:
        super().__init__()

    def name(self) -> str:
        return 'Shell'

    def frame_frequency(self) -> int:
        return 55

    def _do_sort(self, data: data_store) -> None:
        n = data.size()
        interval = n // 2
        while interval > 0:
            for i in range(interval, n):
                temp = data[i]
                j = i
                while j >= interval and data[j - interval] > temp:
                    data[j] = data[j - interval]
                    j -= interval

                data[j] = temp
            interval //= 2
