#!/usr/bin/python3

import os
import random

from cv2 import VideoWriter, VideoWriter_fourcc

from sort_video.image_tools import draw_image
from sort_video.data_tools import data_store

from sorters.sort_base import sort_base
from sorters.insertion import insertion_sort
from sorters.selection import selection_sort
from sorters.bubble import bubble_sort


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
    size = 10000
    folder = 'output'
    rand_data = random.sample(range(0, size), size)
    sorters = [insertion_sort(), selection_sort(), bubble_sort()]
    for sorter in sorters:
        make_video(folder, sorter, rand_data.copy())
