#!/usr/bin/python3

from sorters.sort_base import sort_base
from sort_util.data_tools import data_store


class merge_sort(sort_base):
    def __init__(self) -> None:
        super().__init__()
        self.draw_counter = 0

    def name(self) -> str:
        return 'Merge'

    def _do_sort(self, data: data_store) -> None:
        self.__merge_sort(data, 0, data.size() - 1)

    def __merge_sort(self, data: data_store, left: int, right: int) -> None:
        if left < right:
            mid = int(left + (right - left) / 2)
            self.__merge_sort(data, left, mid)
            self.__merge_sort(data, mid + 1, right)
            self.__merge(data, left, mid, right)

    def __merge(self, data: data_store, start: int, mid: int, end: int) -> None:
        start2 = mid + 1
        if(data[mid] <= data[start2]):
            return
        while start <= mid and start2 <= end:
            if data.is_less_than(start, start2):
                start += 1
            else:
                data.move(start2, start)
                start += 1
                mid += 1
                start2 += 1

                self.draw_counter += 1
                if self.draw_counter % 4 == 0:
                    data.draw(self.name())
