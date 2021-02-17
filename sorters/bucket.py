#!/usr/bin/python3

from sorters.sort_base import sort_base
from sort_util.data_tools import data_store


class bucket_sort(sort_base):
    def __init__(self) -> None:
        super().__init__()

    def name(self) -> str:
        return 'Bucket'

    def __insertion_sort__(self, data: data_store, start: int, end: int):
        for i in range(start, end):
            src_index = i
            for j in range(0, i):
                if data.is_less_than(src_index, j):
                    data.move(src_index, j)
                    break

    def _do_sort(self, data: data_store) -> None:
        bucket_size = 50
        num_buckets = int(data.size() / bucket_size)
        if num_buckets == 0:
            self.__insertion_sort__(data, 0, data.size())
            return

        bucket_sizes = [0] * num_buckets

        for i in range(data.size()):
            bucket_idx = int(data[i] / bucket_size)
            dest_idx = sum(bucket_sizes[0: bucket_idx + 1])
            data.move(i, dest_idx)
            bucket_sizes[bucket_idx] += 1

        for i in range(num_buckets - 1, -1, -1):
            start = sum(bucket_sizes[0: i])
            end = start + bucket_sizes[i]
            self.__insertion_sort__(data, start, end)
