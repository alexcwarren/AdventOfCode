import pytest

import tuning_trouble


@pytest.fixture
def script():
    return tuning_trouble.TuningTrouble("sample.in")


def test_sample_input_part1(script):
    assert script.get_start_of_packet() == 7


def test_sample_input_part2(script):
    assert script.get_start_of_message() == 19
