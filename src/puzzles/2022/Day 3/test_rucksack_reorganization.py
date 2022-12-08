import pytest

import rucksack_reorganization


@pytest.fixture
def script():
    return rucksack_reorganization.RucksackReorganization("sample.in")


def test_sample_input(script):
    assert script.sum_shared_item_priorities() == 157


def test_actual_input(script):
    pass
