"""Test for task2."""

import pytest

from task2 import degree

test_cases = (
    (5.0, 2.0, 3.0, 4.0, 0)
), (
    (5.0, 1.0, 3.0, 4.0, 180)
), (
    (0, 1.0, 3.0, 4.0, 0)
)


@pytest.mark.parametrize('radius, accel, time, velocity, expected', test_cases)
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
