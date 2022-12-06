import pytest

import calorie_counting


@pytest.fixture
def script():
    return calorie_counting.CalorieCounter("sample.in")


def test_sample_input(script):
    assert script.find_most_calories() == 24000
