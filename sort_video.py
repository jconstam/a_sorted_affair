#!/usr/bin/python3

import os
import random
import argparse

from cv2 import VideoWriter, VideoWriter_fourcc

from sort_video.image_tools import draw_image
from sort_video.data_tools import data_store

from sorters.sort_base import sort_base
from sorters.insertion import insertion_sort
from sorters.selection import selection_sort
from sorters.bubble import bubble_sort
from sorters.merge import merge_sort

INSERT_NAME = 'Insertion'
SELECT_NAME = 'Selection'
BUBBLE_NAME = 'Bubble'
MERGE_NAME = 'Merge'

short_names = {
    INSERT_NAME: ['ins', 'insert', 'insertion'],
    SELECT_NAME: ['sel', 'select', 'selection'],
    BUBBLE_NAME: ['bub', 'bubble'],
    MERGE_NAME: ['merge']
}
alg_classes = {
    INSERT_NAME: insertion_sort,
    SELECT_NAME: selection_sort,
    BUBBLE_NAME: bubble_sort,
    MERGE_NAME: merge_sort
}


def make_video(folder: str, sorter: sort_base, rand_data: list) -> None:
    width = 3840
    height = 2160
    fps = 60
    size = len(rand_data)

    drawer = draw_image(width, height, size)
    raw_file_name = os.path.join(
        folder, 'sorted_{}_{}.mp4'.format(size, sorter.name()))
    final_file_name = os.path.join(
        folder, 'sorted_{}_{}.mkv'.format(size, sorter.name()))
    video = VideoWriter(raw_file_name, VideoWriter_fourcc(*'mp4v'), float(fps), (width, height))

    store = data_store(drawer, video)
    store.load(rand_data)
    sorter.sort(store)

    video.release()

    store.convert(raw_file_name, final_file_name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate videos of sorting algorithms in action')
    parser.add_argument('-s', '--size', type=int, default=1000, help='The size of the array to be sorted')
    parser.add_argument('-o', '--outputFolder', type=str, default='output/', help='The path to put the videos')
    parser.add_argument('algorithms', metavar='alg', type=str, nargs='+', help='Sorting algorithms to run')
    args = parser.parse_args()

    folder = os.path.abspath(args.outputFolder)
    assert os.path.exists(folder), 'Output path does not exist'

    print('Sorting arrays of {} elements'.format(args.size))
    print('Output will be located in "{}"'.format(folder))
    sorters = []
    for alg in args.algorithms:
        for key, value in short_names.items():
            if alg.lower() in value:
                print('Using sort algorithm "{}"'.format(key))
                sorters.append(alg_classes[key]())
                break
        else:
            raise Exception('Algorithm {} not found'.format(alg))

    rand_data = random.sample(range(0, args.size), args.size)
    for sorter in sorters:
        make_video(folder, sorter, rand_data.copy())
