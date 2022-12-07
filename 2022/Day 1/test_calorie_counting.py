import pytest

import calorie_counting


@pytest.fixture
def script():
    return calorie_counting.CalorieCounter("sample.in")


def test_sample_input_part1(script):
    assert script.find_most_calories() == 24000


def test_sample_input_part2(script):
    assert script.find_top3_most_calories() == 45000
