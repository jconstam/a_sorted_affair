#!/usr/bin/python3

import abc 
import datetime

from sort_video import data_tools


class sort_base(abc.ABC):
    def __init__(self) -> None:
        super().__init__()

    @abc.abstractmethod
    def _do_sort(self, data: data_tools.data_store) -> None:
        raise NotImplementedError("Must override __do_sort")

    @abc.abstractmethod
    def _sort_name(self) -> str:
        raise NotImplementedError("Must override __sort_name")

    def sort(self, data: data_tools.data_store) -> None:
        print('Starting sort "{}" with {} items'.format(
            self._sort_name(), data.size()))
        start = datetime.datetime.now()
        self._do_sort(data)
        end = datetime.datetime.now()
        data.done()
        print('Done in {}'.format(end - start))
