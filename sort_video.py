#!/usr/bin/python3

import os
import glob
import random

from cv2 import VideoWriter, VideoWriter_fourcc

from sort_video.image_tools import draw_image
from sort_video.data_tools import data_store

from sorters.sort_base import sort_base
from sorters.insertion import insertion_sort
from sorters.selection import selection_sort


def make_video(sorter: sort_base, rand_data: list):
    folder = 'output'
    width = 3840
    height = 2160
    fps = 60
    size = len(rand_data)

    drawer = draw_image(width, height, size)
    video = VideoWriter(os.path.join(folder, 'sorted_{}_{}.mp4'.format(size, sorter.name())),
                            VideoWriter_fourcc(*'mp4v'), float(fps), (width, height))

    store = data_store(drawer, video)
    store.load(rand_data)

    sorter.sort(store)

    video.release()

if __name__ == '__main__':
    size = 3000
    rand_data = random.sample(range(0, size), size)
    make_video(insertion_sort(), rand_data.copy())
    make_video(selection_sort(), rand_data.copy())
