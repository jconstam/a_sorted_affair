#!/usr/bin/python3

import pytest
import random

from sorters.sort_base import sort_base
from sort_util.data_tools import data_store

normal_test_size = 100
big_test_size = 1000

def check_sorted(sorter: sort_base, data):
    store = data_store(None, None)
    store.load(data, "Test Data")
    sorted_data = sorted(data.copy())
    sorter.sort(store)

    assert set(sorted_data) == set(store)


def test__sort__empty(sorter: sort_base) -> None:
    with pytest.raises(AssertionError):
        check_sorted(sorter, [])

def test__sort__singleton(sorter: sort_base) -> None:
    check_sorted(sorter, [0])

def test__sort__presorted(sorter: sort_base):
    check_sorted(sorter, list(range(0, normal_test_size)))

def test__sort__reverse_sorted(sorter: sort_base):
    check_sorted(sorter, list(range(normal_test_size, 0, -1)))

def test__sort__random(sorter: sort_base):
    for i in range(0, normal_test_size):
        check_sorted(sorter, random.sample(
            range(0, normal_test_size), normal_test_size))

def test__sort__random_big(sorter: sort_base):
    check_sorted(sorter, list(range(0, big_test_size)))
