"""Tester degree calculator module."""
import pytest

from main import degree

degree_test_data = (
    (1.555, 3, 7, 1, 86.12),
    (1.895, 4.5, 8.7, 3.2, 230.89),
    (5, 1, 6, 9, 105.06),
    (2.375, 0, 1.0, 6.0, 144.75),
    (0, 65.0, 5.5, 3.0, -1.0),
    (-38, 0, 5.0, 3.0, -1.0),
    (1.567, 'noskov', 5.0, 3.0, -1.0),
)


@pytest.mark.parametrize('rad, accel, time, vel, expected', degree_test_data)
def test_degrees(rad: float, accel: float, time: float, vel: float, expected: float) -> None:
    """Test degree function with degree_test_data.

    Args:
        rad: float - current value for radius variable of degree function
        accel: float - current value for acceleration variable of degree function
        time: float - current value for time variable of degree function
        vel: float - current value for velocity variable of degree function
        expected: float - current expected answer of degree function

    Asserts:
        true if degree returns expected answer
    """
    assert round(degree(rad, accel, time, vel), 2) == expected
