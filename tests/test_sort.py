#!/usr/bin/python3

import pytest

from sorters.sort import sort

from sorters.insertion import insertion_sort
from sorters.selection import selection_sort
from sorters.bubble import bubble_sort
from sorters.merge import merge_sort
from sorters.quick import quick_sort
from sorters.radix import radix_sort
from sorters.heap import heap_sort


def test__sort_classes():
    alg_classes = sort.get_alg_classes()
    assert alg_classes['Insertion'] == insertion_sort
    assert alg_classes['Selection'] == selection_sort
    assert alg_classes['Bubble'] == bubble_sort
    assert alg_classes['Merge'] == merge_sort
    assert alg_classes['Quick'] == quick_sort
    assert alg_classes['Radix'] == radix_sort
    assert alg_classes['Heap'] == heap_sort

def test__sort_short_names():
    alg_short_names = sort.get_alg_short_names()
    assert alg_short_names['Insertion']
    assert alg_short_names['Selection']
    assert alg_short_names['Bubble']
    assert alg_short_names['Merge']
    assert alg_short_names['Quick']
    assert alg_short_names['Radix']
    assert alg_short_names['Heap']
