import os
import pytest

from sort_util.image_tools import draw_image
from sort_util.data_tools import data_store
from sorters.insertion import insertion_sort

from cv2 import VideoWriter, VideoWriter_fourcc

test_folder = 'pytest_output'
test_file = os.path.join(test_folder, 'test.avi')

test_data_in = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def setup_function():
    os.makedirs(test_folder)
    pass

def teardown_function():
    os.remove(test_file)
    os.rmdir(test_folder)
    pass


@pytest.fixture
def testData():
    drawer = draw_image(100, 100, 10)
    video = VideoWriter(test_file, VideoWriter_fourcc(
        *'mp4v'), float(60), (100, 100))
    data = data_store(drawer, video)
    data.load(test_data_in, "Test Data")
    return data


def test_sorting(testData):
    sorter = insertion_sort()
    sorter.sort(testData)

    test_data_out = sorted(test_data_in.copy())
    for i in range(len(test_data_in)):
        assert test_data_in[i] == test_data_out[i]
