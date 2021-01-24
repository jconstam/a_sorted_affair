#!/usr/bin/python3

from typing import Any
import numpy

from PIL import Image, ImageDraw, ImageFont


class draw_image:
    def __init__(self, width, height, size) -> None:
        self.size = size
        self.bar_width = max(round(width / size), 1)
        self.bar_height_scaler = height / size
        self.width = width
        self.height = height
        self.font_size = int(height / 50)

    def get_image_size(self):
        return (self.width, self.height)

    def __write_text(self, drawer, line, field, value):
        font = ImageFont.truetype(font='FreeMono.ttf', size=self.font_size)
        location = (self.font_size / 2, (line + 0.5) * self.font_size)
        drawer.text(location, '{:20s} {}'.format('{}:'.format(
            field), value), font=font, fill=(255, 255, 255))

    def __get_color(self, value: int):
        vectors = [
            (0, 0, 255),
            (0, 64, 255),
            (0, 255, 255),
            (0, 255, 0),
            (255, 255, 0),
            (255, 0, 0),
            (255, 0, 255)
        ]

        value_scaled = (value / self.size) * (len(vectors) - 1)
        value_idx = int(value_scaled)
        value_frac = value_scaled - value_idx

        b_start, g_start, r_start = vectors[value_idx]
        b_end, g_end, r_end = vectors[value_idx + 1]

        blue = int(((b_end - b_start) * value_frac) + b_start)
        green = int(((g_end - g_start) * value_frac) + g_start)
        red = int(((r_end - r_start) * value_frac) + r_start)

        return (blue, green, red)


    def draw(self, data, name: str) -> Any:
        img = Image.new('RGB', (self.bar_width * self.size, self.height), (0, 0, 0))
        drawer = ImageDraw.Draw(img)

        for i in range(self.size):
            start_x = int((i + 0.5) * self.bar_width)
            start_y = self.height
            end_x = start_x
            end_y = int(self.height - (data[i] * self.bar_height_scaler))
            drawer.line((start_x, start_y, end_x, end_y),
                        fill=self.__get_color(data[i]), width=int(self.bar_width))
        
        img = img.resize((self.width, self.height))

        drawer = ImageDraw.Draw(img)
        self.__write_text(drawer, 0, 'Algorithm', name)
        self.__write_text(drawer, 1, 'Percent Sorted', '{:0.2f}%'.format(data.sortedness()))
        self.__write_text(drawer, 2, 'Array Size', data.size())
        self.__write_text(drawer, 3, 'Array Accesses', data.accesses)
        self.__write_text(drawer, 4, 'Array Swaps', data.swaps)
        self.__write_text(drawer, 5, 'Array Compares', data.compares)
        self.__write_text(drawer, 6, 'Array Moves', data.moves)

        return numpy.array(img)
