#!/usr/bin/python3

from sorters.sort_base import sort_base
from sort_util.data_tools import data_store


class heap_sort(sort_base):
    def __init__(self) -> None:
        super().__init__()

    def name(self) -> str:
        return 'Heap'

    def _do_sort(self, data: data_store) -> None:
        size = data.size()
        for i in range(size // 2 - 1, -1, -1):
            self._heapify(data, size, i)
        for i in range(size - 1, 0, -1):
            data.swap(i, 0)
            self._heapify(data, i, 0)

    def _heapify(self, data: data_store, size: int, root: int) -> None:
        largest = root
        left = (2 * root) + 1
        right = (2 * root) + 2

        if left < size and data[largest] < data[left]:
            largest = left

        if right < size and data[largest] < data[right]:
            largest = right

        if largest != root:
            data.swap(root, largest)
            self._heapify(data, size, largest)
