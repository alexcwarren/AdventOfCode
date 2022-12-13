import pytest

import supply_stacks


@pytest.fixture
def script():
    return supply_stacks.SupplyStacks("sample.in")


def test_sample_input_part1(script):
    assert script.get_crates_on_top() == "CMZ"


def test_sample_input_part2(script):
    pass
