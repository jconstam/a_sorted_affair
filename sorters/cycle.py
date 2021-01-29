#!/usr/bin/python3

from sorters.sort_base import sort_base
from sort_util.data_tools import data_store


class cycle_sort(sort_base):
    def __init__(self) -> None:
        super().__init__()

    def name(self) -> str:
        return 'Cycle'

    def frame_frequency(self) -> int:
        return 2

    def _do_sort(self, data: data_store) -> None:
        for cycle_start in range(0, data.size() - 1):
            item = data[cycle_start]

            pos = cycle_start
            for i in range(cycle_start + 1, data.size()):
                if data.is_less_than(i, cycle_start):
                    pos += 1

            if pos == cycle_start:
                continue

            # Uncomment when there are repeated values
            # while item == data[pos]:
            #     pos += 1
            #     data.swap(pos, cycle_start)

            while pos != cycle_start:
                pos = cycle_start
                for i in range(cycle_start + 1, data.size()):
                    if data.is_less_than(i, cycle_start):
                        pos += 1

                # Uncomment when there are repeated values
                # while item == data[pos]:
                #     pos += 1
                data.swap(pos, cycle_start)

