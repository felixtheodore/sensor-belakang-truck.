import pytest
from distance_checker import evaluate_distance

def test_evaluate_distance_valid_ranges():
    assert evaluate_distance(550) == "OUT_OF_RANGE"
    assert evaluate_distance(350) == "AMAN"
    assert evaluate_distance(150) == "WASPADA"
    assert evaluate_distance(50) == "BAHAYA"

def test_evaluate_distance_boundaries():
    assert evaluate_distance(300) == "AMAN"
    assert evaluate_distance(100) == "WASPADA"

def test_evaluate_distance_invalid_inputs():
    with pytest.raises(ValueError):
        evaluate_distance(-10)
    with pytest.raises(ValueError):
        evaluate_distance("seratus")