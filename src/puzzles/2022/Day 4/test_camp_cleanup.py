import pytest

import camp_cleanup


@pytest.fixture
def script():
    return camp_cleanup.CampCleanup("sample.in")


def test_sample_input_part1(script):
    pass


def test_sample_input_part2(script):
    pass
