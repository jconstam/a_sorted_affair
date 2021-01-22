import os
import pytest

from sort_util.data_tools import data_store
from sorters.sort_base import sort_base
from sorters.insertion import insertion_sort

def setup_function():
    pass

def teardown_function():
    pass


def check_sorted(sorter: sort_base, data):
    store = data_store(None, None)
    store.load(data, "Test Data")
    sorted_data = sorted(data.copy())
    sorter.sort(store)

    for i in range(len(sorted_data)):
        assert sorted_data[i] == sorted_data[i]

def test__sort__presorted():
    check_sorted(insertion_sort(), list(range(0, 100)))


def test__sort__reverse_sorted():
    check_sorted(insertion_sort(), list(range(100, 0, -1)))
