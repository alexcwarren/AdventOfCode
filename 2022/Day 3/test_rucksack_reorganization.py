import pytest

import rucksack_reorganization


@pytest.fixture
def script():
    return rucksack_reorganization.RucksackReorganization("sample.in")


def test_sample_input(script):
    pass


def test_actual_input(script):
    pass
