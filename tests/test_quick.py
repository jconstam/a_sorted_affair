#!/usr/bin/python3

from . import common
from sorters.quick import quick_sort

def test__name():
    assert quick_sort().name() == 'Quick'

def test__sort__empty():
    common.test__sort__empty(quick_sort())

def test__sort__singleton():
    common.test__sort__singleton(quick_sort())

def test__sort__presorted():
    common.test__sort__presorted(quick_sort())

def test__sort__reverse_sorted():
    common.test__sort__reverse_sorted(quick_sort())

def test__sort__random():
    common.test__sort__random(quick_sort())

def test__sort__random_big():
    common.test__sort__random_big(quick_sort())