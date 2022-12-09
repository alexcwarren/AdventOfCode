import pytest

import rucksack_reorganization


@pytest.fixture
def script():
    return rucksack_reorganization.RucksackReorganization("sample.in")


def test_sample_input_part1(script):
    assert script.sum_shared_item_priorities() == 157


def test_sample_input_part2(script):
    assert script.sum_group_type_item_priorities() == 70
