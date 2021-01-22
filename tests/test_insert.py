from . import common
from sorters.insertion import insertion_sort

def test__name():
    assert insertion_sort().name() == 'Insertion'

def test__sort__presorted():
    common.test__sort__presorted(insertion_sort())

def test__sort__reverse_sorted():
    common.test__sort__reverse_sorted(insertion_sort())

def test__sort__random():
    common.test__sort__random(insertion_sort())
