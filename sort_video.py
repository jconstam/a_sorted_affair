#!/usr/bin/python3

import random

from sort_video import image_tools

if __name__ == '__main__':
    size = 500
    width = 3840
    height = 2160
    rands = random.sample(range(0, size), size)

    img = image_tools.draw_image(width, height, size)
    img.draw(rands, 'test.png')
