import pytest

import rock_paper_scissors


@pytest.fixture
def script():
    return rock_paper_scissors.RockPaperScissors("sample.in")


def test_sample_input(script):
    assert script.determine_total_score() == 15


def test_actual_input(script):
    pass
