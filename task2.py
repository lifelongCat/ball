"""Calculates the angle of displacement of a ball on a flat surface."""


from math import ceil, pi

AREA_CIRCUS = 360


def degree(radius: float, acceleration: float, time: float, velocity: float = 0) -> float:
    """Extract the degree of offset of the intersection point.

    Args:
        radius: radius of the ball.
        acceleration: accerleration of the ball.
        time: the time at which the ball moves.
        velocity: Sped which ball moves.

    Returns:
        float: a shift of a dot of the ball, degrees.
    """
    square = velocity * time + (acceleration * time**2) / 2
    circumference = 2 * pi * radius
    if circumference == 0:
        return 0
    offset_angle = ceil(AREA_CIRCUS * (square % circumference))
    if abs(offset_angle) <= AREA_CIRCUS:
        return offset_angle
    return abs(offset_angle) % AREA_CIRCUS
