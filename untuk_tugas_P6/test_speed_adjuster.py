import pytest
from speed_adjuster import calculate_dynamic_threshold

def test_speed_adjuster_normal_speed():
    assert calculate_dynamic_threshold(100.0, 4.0) == 100.0
    assert calculate_dynamic_threshold(100.0, 5.0) == 100.0

def test_speed_adjuster_high_speed():
    assert calculate_dynamic_threshold(100.0, 8.0) == 150.0
    assert calculate_dynamic_threshold(100.0, 10.0) == 150.0

def test_speed_adjuster_invalid_inputs():
    with pytest.raises(ValueError):
        calculate_dynamic_threshold(100.0, -5.0)
    with pytest.raises(ValueError):
        calculate_dynamic_threshold(100.0, "invalid")