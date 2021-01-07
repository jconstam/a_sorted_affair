#!/usr/bin/python3

import abc 
import datetime

from sort_util.data_tools import data_store


class sort_base(abc.ABC):
    def __init__(self) -> None:
        super().__init__()

    @abc.abstractmethod
    def _do_sort(self, data: data_store) -> None:
        raise NotImplementedError("Must override __do_sort")

    @abc.abstractmethod
    def name(self) -> str:
        raise NotImplementedError("Must override __sort_name")

    def sort(self, data: data_store) -> None:
        print('Starting sort "{}" with {} items'.format(
            self.name(), data.size()))
        start = datetime.datetime.now()
        self._do_sort(data)
        end = datetime.datetime.now()
        print('\tDone in {}'.format(end - start))
        data.draw(self.name())
