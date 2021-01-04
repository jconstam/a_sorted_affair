#!/usr/bin/python3

import numpy

from PIL import Image, ImageDraw


class draw_image:
    def __init__(self, width, height, size) -> None:
        self.width = width
        self.height = height
        self.size = size
        self.bar_width = self.width / self.size
        self.bar_height_scaler = self.height / self.size

    def draw(self, data):
        img = Image.new('RGB', (self.width, self.height), (255, 255, 255))
        draw = ImageDraw.Draw(img)

        for i in range(self.size):
            start_x = i*self.bar_width + (0.5 * self.bar_width)
            start_y = self.height
            end_x = start_x
            end_y = data[i] * self.bar_height_scaler
            draw.line((start_x, start_y, end_x, end_y),
                      fill=(0, 0, 0), width=int(self.bar_width))

        return numpy.array(img)
