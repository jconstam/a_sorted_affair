#!/usr/bin/python3

import os
import math
import random
import argparse

from enum import Enum

from cv2 import VideoWriter, VideoWriter_fourcc

from sort_util.image_tools import draw_image
from sort_util.data_tools import data_store

from sorters.sort import sort
from sorters.sort_base import sort_base


class data_type(Enum):
    random = 1,
    reverse = 2,
    saw4 = 3,
    saw8 = 4,
    saw4rev = 5,
    saw8rev = 6,
    sin = 7,
    sin2 = 8,
    sin4 = 9


data_types = {
    'random': data_type.random,
    'reverse': data_type.reverse,
    'saw4': data_type.saw4,
    'saw8': data_type.saw8,
    'saw4rev': data_type.saw4rev,
    'saw8rev': data_type.saw8rev,
    'sin': data_type.sin,
    'sin2': data_type.sin2,
    'sin4': data_type.sin4
}


def make_video(folder: str, sorter: sort_base, data_type_name: str, data: list, width: int, height: int, fps: int, target_len: float) -> None:
    size = len(data)

    drawer = draw_image(width, height, size)
    raw_file_name = os.path.join(
        folder, '{}_{}_{}.avi'.format(sorter.name(), size, data_type_name))
    final_file_name = os.path.join(
        folder, '{}_{}_{}.mkv'.format(sorter.name(), size, data_type_name))
    video = VideoWriter(raw_file_name, VideoWriter_fourcc(*'mp4v'), float(fps),
                        drawer.get_image_size())

    store = data_store(drawer, video)
    store.load(data)
    sorter.sort(store)

    video.release()

    store.convert(raw_file_name, final_file_name)
    store.adjust_length(final_file_name, target_len, fps)


def __get_data_saw__(size: int, mult: int, reverse: bool):
    raw = range(int(size / mult)) if not reverse else range(int(size / mult) - 1, -1, -1)
    return list([x * mult for x in raw]) * mult


def __get_data_sin__(size: int, mult: int):
    data = []
    for i in range(size):
        data.append(int((size / 2) * (math.sin(mult * i / (size / (2 * math.pi))) + 1)))
        if data[i] == size:
            data[i] -= 1
    return data


def get_data(data_type_name: str, size: int):
    data_type_val = data_types[data_type_name]
    if data_type_val == data_type.random:
        return random.sample(range(0, size), size)
    elif data_type_val == data_type.reverse:
        return list(range(size - 1, -1, -1))
    elif data_type_val == data_type.saw4:
        return __get_data_saw__(size, 4, False)
    elif data_type_val == data_type.saw8:
        return __get_data_saw__(size, 8, False)
    elif data_type_val == data_type.saw4rev:
        return __get_data_saw__(size, 4, True)
    elif data_type_val == data_type.saw8rev:
        return __get_data_saw__(size, 8, True)
    elif data_type_val == data_type.sin:
        return __get_data_sin__(size, 1)
    elif data_type_val == data_type.sin2:
        return __get_data_sin__(size, 2)
    elif data_type_val == data_type.sin4:
        return __get_data_sin__(size, 4)
    else:
        return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate videos of sorting algorithms in action')
    parser.add_argument('-s', '--size', type=int, default=10000,
                        help='The size of the array to be sorted')
    parser.add_argument('-o', '--outputFolder', type=str,
                        default='output/', help='The path to put the videos')
    parser.add_argument('-w', '--width', type=int,
                        default=1920, help='The width of the video in pixels')
    parser.add_argument('-g', '--height', type=int,
                        default=1080, help='The height of the video in pixels')
    parser.add_argument('-f', '--fps', type=int,
                        default=60, help='The framerate of the video in frames per second')
    parser.add_argument('-t', '--targetLength', type=float,
                        default=30, help='The target length of the video in seconds')
    parser.add_argument('-d', '--dataType', type=str,
                        default='random', choices=data_types.keys(), help='The type of data to sort')
    parser.add_argument('algorithms', metavar='alg', type=str,
                        nargs='+', help='Sorting algorithms to run')
    args = parser.parse_args()

    folder = os.path.abspath(args.outputFolder)
    if not os.path.exists(folder):
        os.makedirs(folder)

    print('Sorting arrays of {} elements'.format(args.size))
    print('Output will be located in "{}"'.format(folder))
    print('Output will be {}x{} @ {}fps'.format(args.width, args.height, args.fps))
    sorters = []
    alg_classes = sort.get_alg_classes()
    alg_short_names = sort.get_alg_short_names()
    for alg in args.algorithms:
        if alg == 'all':
            for key, value in alg_classes.items():
                print('Using sort algorithm "{}"'.format(key))
                sorters.append(value())
            break
        for key, value in alg_short_names.items():
            if alg.lower() in value:
                print('Using sort algorithm "{}"'.format(key))
                sorters.append(alg_classes[key]())
                break
        else:
            raise Exception('Algorithm {} not found'.format(alg))

    data = get_data(args.dataType, args.size)
    for sorter in sorters:
        make_video(folder, sorter, args.dataType, data.copy(), args.width, args.height, args.fps, args.targetLength)
