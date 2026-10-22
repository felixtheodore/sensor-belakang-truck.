import pytest
from distance_checker import evaluate_distance

def test_distance_checker_valid_ranges():
    assert evaluate_distance(600) == "OUT_OF_RANGE"
    assert evaluate_distance(350) == "AMAN"
    assert evaluate_distance(150) == "WASPADA"
    assert evaluate_distance(50) == "BAHAYA"

def test_distance_checker_boundaries():
    assert evaluate_distance(300) == "AMAN"
    assert evaluate_distance(100) == "WASPADA"

def test_distance_checker_invalid_input():
    with pytest.raises(ValueError):
        evaluate_distance(-5)
    with pytest.raises(ValueError):
        evaluate_distance("invalid")