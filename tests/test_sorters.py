#!/usr/bin/python3

import pytest
import random

from sort_util.data_tools import data_store
from sorters.sort import sort
from sorters.sort_base import sort_base


normal_test_size = 100
big_test_size = 1000


def check_sorted(sorter: sort_base, data):
    store = data_store(None, None)
    store.load(data)
    sorted_data = sorted(data.copy())
    sorter.sort(store)

    assert set(sorted_data) == set(store)


def test__sorters():
    alg_classes = sort.get_alg_classes()
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
        for _ in range(0, normal_test_size):
            check_sorted(alg_class(), random.sample(range(0, normal_test_size), normal_test_size))
        # Test repeating values
        for mult in range(2, 9):
            check_sorted(alg_class(), list(range(int(normal_test_size / mult))) * mult)
        # Test big data store
        check_sorted(alg_class(), list(range(0, big_test_size)))
