#!/usr/bin/python3

import random

from sort_video import image_tools
from sort_video import data_tools

if __name__ == '__main__':
    size = 50
    width = 3840
    height = 2160
    rands = random.sample(range(0, size), size)

    drawer = image_tools.draw_image(width, height, size)

    store = data_tools.data_store(drawer, 'output/testdata.png')
    store.load(rands)

    print(store[0])
    print(store[1])

    store.swap(0, 1)
    print(store[0])
    print(store[1])
