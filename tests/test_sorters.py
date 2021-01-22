#!/usr/bin/python3

import pytest
import random

from sort_util.data_tools import data_store

from sorters.sort_base import sort_base
from sorters.insertion import insertion_sort
from sorters.selection import selection_sort
from sorters.bubble import bubble_sort
from sorters.merge import merge_sort
from sorters.quick import quick_sort
from sorters.radix import radix_sort

INSERT_NAME = 'Insertion'
SELECT_NAME = 'Selection'
BUBBLE_NAME = 'Bubble'
MERGE_NAME = 'Merge'
QUICK_NAME = 'Quick'
RADIX_NAME = 'Radix'

alg_classes = {
    INSERT_NAME: insertion_sort,
    SELECT_NAME: selection_sort,
    BUBBLE_NAME: bubble_sort,
    MERGE_NAME: merge_sort,
    QUICK_NAME: quick_sort,
    RADIX_NAME: radix_sort
}


normal_test_size = 100
big_test_size = 1000


def check_sorted(sorter: sort_base, data):
    store = data_store(None, None)
    store.load(data, "Test Data")
    sorted_data = sorted(data.copy())
    sorter.sort(store)

    assert set(sorted_data) == set(store)


def test__sorters():
    for alg_name, alg_class in alg_classes.items():
        # Test name
        assert alg_class().name() == alg_name
        # Test empty datastore
        with pytest.raises(AssertionError):
            check_sorted(alg_class(), [])
        # Test singleton data store
        check_sorted(alg_class(), [0])
        # Test pre-sorted data store
        check_sorted(alg_class(), list(range(0, normal_test_size)))
        # Test reverse-sorted data store
        check_sorted(alg_class(), list(range(normal_test_size, 0, -1)))
        # Test randomly sorted data stores
        for i in range(0, normal_test_size):
            check_sorted(alg_class(), random.sample(
                range(0, normal_test_size), normal_test_size))
        # Test big data store
        check_sorted(alg_class(), list(range(0, big_test_size)))
