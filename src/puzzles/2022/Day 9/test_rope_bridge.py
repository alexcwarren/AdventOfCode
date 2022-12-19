import pytest
import rope_bridge


@pytest.fixture
def script():
    return rope_bridge.RopeBridge("sample.in")


def test_sample_input_part1(script):
    assert script.solve_part1() == 13


def test_sample_input_part2(script):
    pass
