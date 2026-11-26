import pytest
from distance_checker import evaluate_distance
from speed_adjuster import calculate_dynamic_threshold
from alert_logger import AlertLogger
from report_generator import generate_trip_report
from app import app

# 1. 70 Unit Test: Kecepatan Mundur & Dynamic Threshold
@pytest.mark.parametrize("speed,expected_threshold", [
    (round(i * 0.5, 1), 100.0 if round(i * 0.5, 1) <= 5.0 else 150.0)
    for i in range(70)
])
def test_dynamic_threshold_70_cases(speed, expected_threshold):
    assert calculate_dynamic_threshold(100.0, speed) == expected_threshold


# 2. 70 Unit Test: Evaluasi Jarak & Klasifikasi Status Bahaya
@pytest.mark.parametrize("distance,expected_status", [
    (d, "BAHAYA" if d < 100 else ("WASPADA" if d < 300 else ("AMAN" if d <= 500 else "OUT_OF_RANGE")))
    for d in range(10, 710, 10)
])
def test_evaluate_distance_70_cases(distance, expected_status):
    assert evaluate_distance(float(distance), 100.0) == expected_status


# 3. 30 Unit Test: AlertLogger & Perhitungan Skor Driver
@pytest.mark.parametrize("danger_count", range(30))
def test_logger_and_report_30_cases(danger_count):
    logger = AlertLogger()
    for _ in range(danger_count):
        logger.log_alert(50.0, "BAHAYA", 8.0)
    report = generate_trip_report(logger.get_logs())
    expected_score = max(0, 100 - (danger_count * 10))
    assert report["danger_count"] == danger_count
    assert report["safety_score"] == expected_score


# 4. 30 Unit Test: Endpoint Web Flask (/api/simulate & Validasi Input)
@pytest.mark.parametrize("speed,distance,expected_code", [
    (5.0, 200.0, 200),
    (8.0, 120.0, 200),
    (0.0, 400.0, 200),
    (12.0, 50.0, 200),
    (15.0, 350.0, 200),
] * 4 + [
    (-5.0, 100.0, 400),
    (10.0, -20.0, 400),
    (999.0, 100.0, 400),
    (10.0, 99999.0, 400),
    ("NaN", 100.0, 400),
    (10.0, "Infinity", 400),
    ("", 100.0, 400),
    (10.0, "", 400),
    ("abc", 100.0, 400),
    (10.0, "xyz", 400),
])
def test_flask_api_30_cases(speed, distance, expected_code):
    client = app.test_client()
    res = client.post("/api/simulate", json={"speed": speed, "distance": distance})
    assert res.status_code == expected_code