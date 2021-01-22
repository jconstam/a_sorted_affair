#!/usr/bin/python3

from . import common
from sorters.selection import selection_sort

def test__name():
    assert selection_sort().name() == 'Selection'

def test__sort__empty():
    common.test__sort__empty(selection_sort())

def test__sort__singleton():
    common.test__sort__singleton(selection_sort())

def test__sort__presorted():
    common.test__sort__presorted(selection_sort())

def test__sort__reverse_sorted():
    common.test__sort__reverse_sorted(selection_sort())

def test__sort__random():
    common.test__sort__random(selection_sort())

def test__sort__random_big():
    common.test__sort__random_big(selection_sort())