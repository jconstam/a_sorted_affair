#!/usr/bin/python3

from sorters.sort_base import sort_base
from sorters.insertion import insertion_sort
from sorters.selection import selection_sort
from sorters.bubble import bubble_sort
from sorters.merge import merge_sort
from sorters.quick import quick_sort
from sorters.radix import radix_sort
from sorters.heap import heap_sort
from sorters.comb import comb_sort


class sort:
    __INSERT_NAME = 'Insertion'
    __SELECT_NAME = 'Selection'
    __BUBBLE_NAME = 'Bubble'
    __MERGE_NAME = 'Merge'
    __QUICK_NAME = 'Quick'
    __RADIX_NAME = 'Radix'
    __HEAP_NAME = 'Heap'
    __COMB_NAME = 'Comb'

    __alg_classes = {
        __INSERT_NAME: insertion_sort,
        __SELECT_NAME: selection_sort,
        __BUBBLE_NAME: bubble_sort,
        __MERGE_NAME: merge_sort,
        __QUICK_NAME: quick_sort,
        __RADIX_NAME: radix_sort,
        __HEAP_NAME: heap_sort,
        __COMB_NAME: comb_sort
    }

    __short_names = {
        __INSERT_NAME: ['ins', 'insert', 'insertion'],
        __SELECT_NAME: ['sel', 'select', 'selection'],
        __BUBBLE_NAME: ['bub', 'bubble'],
        __MERGE_NAME: ['merge'],
        __QUICK_NAME: ['quick'],
        __RADIX_NAME: ['radix'],
        __HEAP_NAME: ['heap'],
        __COMB_NAME: ['comb']
    }
    @staticmethod
    def get_alg_classes() -> dict:
        return sort.__alg_classes

    @staticmethod
    def get_alg_short_names() -> dict:
        return sort.__short_names
