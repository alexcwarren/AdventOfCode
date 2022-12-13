import pytest

import no_space_left_on_device


@pytest.fixture
def script():
    return no_space_left_on_device.NoSpaceLeftOnDevice("sample.in")


def test_sample_input_part1(script):
    assert script.sum_sizes_of_directories() == 95437


def test_sample_input_part2(script):
    pass
