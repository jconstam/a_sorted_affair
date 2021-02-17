#!/usr/bin/python3

from sorters.sort import sort

from sorters.insertion import insertion_sort
from sorters.selection import selection_sort
from sorters.bubble import bubble_sort
from sorters.merge import merge_sort
from sorters.quick import quick_sort
from sorters.radix import radix_sort
from sorters.heap import heap_sort
from sorters.comb import comb_sort
from sorters.shell import shell_sort
from sorters.pancake import pancake_sort
from sorters.gnome import gnome_sort
from sorters.bucket import bucket_sort

NUMBER_OF_SORTERS = 12


def test__sort_classes():
    alg_classes = sort.get_alg_classes()
    assert len(alg_classes.keys()) == NUMBER_OF_SORTERS
    assert alg_classes['Insertion'] == insertion_sort
    assert alg_classes['Selection'] == selection_sort
    assert alg_classes['Bubble'] == bubble_sort
    assert alg_classes['Merge'] == merge_sort
    assert alg_classes['Quick'] == quick_sort
    assert alg_classes['Radix'] == radix_sort
    assert alg_classes['Heap'] == heap_sort
    assert alg_classes['Comb'] == comb_sort
    assert alg_classes['Shell'] == shell_sort
    assert alg_classes['Pancake'] == pancake_sort
    assert alg_classes['Gnome'] == gnome_sort
    assert alg_classes['Bucket'] == bucket_sort


def test__sort_short_names():
    alg_short_names = sort.get_alg_short_names()
    assert len(alg_short_names.keys()) == NUMBER_OF_SORTERS
    assert alg_short_names['Insertion']
    assert alg_short_names['Selection']
    assert alg_short_names['Bubble']
    assert alg_short_names['Merge']
    assert alg_short_names['Quick']
    assert alg_short_names['Radix']
    assert alg_short_names['Heap']
    assert alg_short_names['Comb']
    assert alg_short_names['Shell']
    assert alg_short_names['Pancake']
    assert alg_short_names['Gnome']
    assert alg_short_names['Bucket']
