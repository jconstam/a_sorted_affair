import random

from sorters.sort_base import sort_base
from sort_util.data_tools import data_store

def check_sorted(sorter: sort_base, data):
    store = data_store(None, None)
    store.load(data, "Test Data")
    sorted_data = sorted(data.copy())
    sorter.sort(store)

    for i in range(len(sorted_data)):
        assert sorted_data[i] == sorted_data[i]

def test__sort__presorted(sorter: sort_base):
    check_sorted(sorter, list(range(0, 100)))


def test__sort__reverse_sorted(sorter: sort_base):
    check_sorted(sorter, list(range(100, 0, -1)))


def test__sort__random(sorter: sort_base):
    for i in range(0, 100):
        check_sorted(sorter, random.sample(range(0, 100), 100))
