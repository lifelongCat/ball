import pytest
from main import degree
 
degree_test_data = ( 
    (1.555, 3.0, 7.0, 1.0), 
    (1.895, 4.0, 9.0, 3.0), 
    (2.375, 5.0, 1.0, 6.0), 
    (4.500, 1.0, 6.0, 9.0),
    (1.592, 0.5, 5.0, 3.0),
    (0, 65.0, 5.0, 3.0),
    (-38, 0.0, 5.0, 3.0, -1.0),
    (1.567, "noskov", 5.0, 3.0, -1.0),  
) 
 
@pytest.mark.parametrize('radius, acceleration, time, velocity, expected', degree_test_data) 
def test_degrees(radius: float, acceleration: float, time: float, velocity: float, expected: float) -> None: 
    assert round(degree(radius, acceleration, time, velocity), 2) == expected