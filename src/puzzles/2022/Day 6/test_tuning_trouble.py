import pytest

import tuning_trouble


@pytest.fixture
def script():
    return tuning_trouble.TuningTrouble("sample.in")


def test_sample_input_part1(script):
    pass


def test_sample_input_part2(script):
    pass
