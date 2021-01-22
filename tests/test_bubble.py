#!/usr/bin/python3

from . import common
from sorters.bubble import bubble_sort

def test__name():
    assert bubble_sort().name() == 'Bubble'

def test__sort__empty():
    common.test__sort__empty(bubble_sort())

def test__sort__singleton():
    common.test__sort__singleton(bubble_sort())

def test__sort__presorted():
    common.test__sort__presorted(bubble_sort())

def test__sort__reverse_sorted():
    common.test__sort__reverse_sorted(bubble_sort())

def test__sort__random():
    common.test__sort__random(bubble_sort())

def test__sort__random_big():
    common.test__sort__random_big(bubble_sort())