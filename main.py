"""Degree calculator module."""
from math import pi


def degree(radius: float, acceleration: float, time: float, velocity: float = 0) -> float:
    """Calculate offset angle.

    Args:
        radius: float - ball radius
        acceleration: float - ball acceleration
        time: float - ball movement time
        velocity: float - ball velocity

    Returns:
        float - answer if all data is correct else -1.0
    """
    full_circle = 360
    var_types = set(map(type, [radius, acceleration, time, velocity]))
    if var_types - {int, float} != set():
        return -1.0
    if radius <= 0 or acceleration < 0 or time <= 0 or velocity <= 0:
        return -1.0
    distance = velocity * time + (acceleration * time * time) / 2
    circ_length = 2 * pi * radius
    return (distance % circ_length) / circ_length * full_circle
