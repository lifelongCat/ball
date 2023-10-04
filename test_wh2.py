"""Test for test_wh2."""

import pytest

from task2 import degree

TEST_CASES = (
    (5.0, 2.0, 3.0, 4.0, 0)
), (
    (5.0, 1.0, 3.0, 4.0, 180)
), (
    (0, 1.0, 3.0, 4.0, 0)
)


@pytest.mark.parametrize('radius, accel, time, velocity, expected', TEST_CASES)
def test_degree(radius: float, accel: float, time: float, velocity: float, expected: int) -> None:
    """Test our degree function.

    Args:
        radius: radius of the ball.
        accel: accerleration of the ball.
        time: the time at which the ball moves.
        velocity: speed which ball moves.
        expected: - expected answer.

    Asserts:
        True if answer is correct
    """
    assert degree(radius, accel, time, velocity) == expected
