import pytest
from speed_adjuster import calculate_dynamic_threshold

def test_speed_adjuster_normal_and_fast():
    assert calculate_dynamic_threshold(100, 3.0) == 100.0
    assert calculate_dynamic_threshold(100, 8.0) == 150.0

def test_speed_adjuster_invalid_input():
    with pytest.raises(ValueError):
        calculate_dynamic_threshold(100, -2)
    with pytest.raises(ValueError):
        calculate_dynamic_threshold(-50, 5)