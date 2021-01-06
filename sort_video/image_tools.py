#!/usr/bin/python3

from typing import Any
import numpy

from PIL import Image, ImageDraw, ImageFont


class draw_image:
    def __init__(self, width, height, size) -> None:
        self.width = width
        self.height = height
        self.size = size
        self.bar_width = self.width / self.size
        self.bar_height_scaler = self.height / self.size

    def __write_text(self, drawer, line, field, value):
        font_size = 36
        font = ImageFont.truetype(font='FreeMono.ttf', size=font_size)
        location = (font_size / 2, (line + 0.5) * font_size)
        drawer.text(location, '{:20s} {}'.format('{}:'.format(field), value), font=font, fill=(0, 0, 0))


    def draw(self, data, name: str) -> Any:
        img = Image.new('RGB', (self.width, self.height), (255, 255, 255))
        drawer = ImageDraw.Draw(img)
        self.__write_text(drawer, 0, 'Algorithm', name)
        self.__write_text(drawer, 1, 'Array Size', data.size())
        self.__write_text(drawer, 2, 'Array Accesses', data.accesses)
        self.__write_text(drawer, 3, 'Array Swaps', data.swaps)
        self.__write_text(drawer, 4, 'Array Compares', data.compares)
        self.__write_text(drawer, 5, 'Array Moves', data.moves)

        for i in range(self.size):
            start_x = (i + 0.5) * self.bar_width
            start_y = self.height
            end_x = start_x
            end_y = self.height - (data[i] * self.bar_height_scaler)
            drawer.line((start_x, start_y, end_x, end_y),
                      fill=(0, 0, 0), width=int(self.bar_width))

        return numpy.array(img)
