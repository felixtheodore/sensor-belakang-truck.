from report_generator import generate_trip_report

def test_report_generator_scoring():
    sample_logs = [
        {"distance": 400, "status": "AMAN"},
        {"distance": 150, "status": "WASPADA"},
        {"distance": 50, "status": "BAHAYA"},
        {"distance": 40, "status": "BAHAYA"}
    ]
    report = generate_trip_report(sample_logs)

    assert report["total_events"] == 4
    assert report["danger_count"] == 2
    assert report["warning_count"] == 1
    assert report["safety_score"] == 78
    assert report["rating"] == "GOOD"