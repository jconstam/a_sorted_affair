#!/usr/bin/python3

import os
import glob
import random

import cv2
import numpy

from PIL import Image

from sort_video import image_tools
from sort_video import data_tools

from sorters import insertion

if __name__ == '__main__':
    folder = 'output'
    files = glob.glob('{}/*'.format(folder))
    for f in files:
        os.remove(f)

    size = 20
    width = 3840
    height = 2160
    fps = 100
    rands = random.sample(range(0, size), size)

    drawer = image_tools.draw_image(width, height, size)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter('{}/testdata.mp4'.format(folder),
                            fourcc, float(fps), (width, height))

    store = data_tools.data_store(drawer, video)
    store.load(rands)

    insertion.sort(store)

    video.release()
