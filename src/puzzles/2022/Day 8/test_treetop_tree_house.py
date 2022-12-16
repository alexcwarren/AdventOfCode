import pytest

import treetop_tree_house


@pytest.fixture
def script():
    return treetop_tree_house.TreetopTreeHouse("sample.in")


def test_sample_input_part1(script):
    assert script.solve_part1() == 21


def test_sample_input_part2(script):
    assert script.solve_part2() == 8
