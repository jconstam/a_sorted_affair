#!/usr/bin/python3

from sort_video import data_tools

def sort(data:data_tools.data_store):
    print('Starting insertion sort with {} items'.format(data.size()))
    sorted = False
    while not sorted:
        sorted = True
        for index in range(data.size() - 1):
            if data.is_less_than(index, index + 1):
                data.swap(index, index + 1)
                sorted = False
    data.done()
    print('Done')
