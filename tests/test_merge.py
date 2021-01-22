#!/usr/bin/python3

from . import common
from sorters.merge import merge_sort

def test__name():
    assert merge_sort().name() == 'Merge'

def test__sort__empty():
    common.test__sort__empty(merge_sort())

def test__sort__singleton():
    common.test__sort__singleton(merge_sort())

def test__sort__presorted():
    common.test__sort__presorted(merge_sort())

def test__sort__reverse_sorted():
    common.test__sort__reverse_sorted(merge_sort())

def test__sort__random():
    common.test__sort__random(merge_sort())

def test__sort__random_big():
    common.test__sort__random_big(merge_sort())