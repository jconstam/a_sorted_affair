#!/usr/bin/python3

import os
import glob
import random

from cv2 import VideoWriter, VideoWriter_fourcc

from sort_video.image_tools import draw_image
from sort_video.data_tools import data_store

from sorters.sort_base import sort_base
from sorters.insertion import insertion_sort


def make_video(sorter: sort_base, size):
    folder = 'output'
    width = 3840
    height = 2160
    fps = 100

    rands = random.sample(range(0, size), size)
    drawer = draw_image(width, height, size)
    video = VideoWriter(os.path.join(folder, 'sorted_{}_{}.mp4'.format(size, sorter.name())),
                            VideoWriter_fourcc(*'mp4v'), float(fps), (width, height))

    store = data_store(drawer, video)
    store.load(rands)

    sorter.sort(store)

    video.release()

if __name__ == '__main__':
    size = 50
    make_video(insertion_sort(), size)
