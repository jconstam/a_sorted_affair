#!/usr/bin/python3

from . import common
from sorters.radix import radix_sort

def test__name():
    assert radix_sort().name() == 'Radix'

def test__sort__empty():
    common.test__sort__empty(radix_sort())

def test__sort__singleton():
    common.test__sort__singleton(radix_sort())

def test__sort__presorted():
    common.test__sort__presorted(radix_sort())

def test__sort__reverse_sorted():
    common.test__sort__reverse_sorted(radix_sort())

def test__sort__random():
    common.test__sort__random(radix_sort())

def test__sort__random_big():
    common.test__sort__random_big(radix_sort())