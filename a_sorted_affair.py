#!/usr/bin/python3

import os
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
    reverse = 2

data_types = {
    'random': data_type.random,
    'reverse': data_type.reverse
}


def make_video(folder: str, sorter: sort_base, data_type_name: str, data: list, width: int, height: int, fps: int) -> None:
    size = len(data)

    drawer = draw_image(width, height, size)
    raw_file_name = os.path.join(
        folder, '{}_{}_{}.avi'.format(sorter.name(), size, data_type_name))
    final_file_name = os.path.join(
        folder, '{}_{}_{}.mkv'.format(sorter.name(), size, data_type_name))
    video = VideoWriter(raw_file_name, VideoWriter_fourcc(*'mp4v'), float(fps),
                        drawer.get_image_size())

    store = data_store(drawer, video)
    store.load(data, sorter.name())
    sorter.sort(store)

    video.release()

    store.convert(raw_file_name, final_file_name)

def get_data(data_type_name: str, size: int):
    data_type = data_types[data_type_name]
    if data_type == data_type.random:
        return random.sample(range(0, size), size)
    elif data_type == data_type.reverse:
        return list(range(size - 1, -1, -1))
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
        make_video(folder, sorter, args.dataType, data.copy(), args.width, args.height, args.fps)
