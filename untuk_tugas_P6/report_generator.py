def generate_trip_report(logs):
    if not logs:
        return {
            "total_events": 0,
            "danger_count": 0,
            "warning_count": 0,
            "safety_score": 100,
            "rating": "EXCELLENT (NO DATA)"
        }

    total_events = len(logs)
    danger_count = sum(1 for log in logs if log["status"] == "BAHAYA")
    warning_count = sum(1 for log in logs if log["status"] == "WASPADA")

    # Formula Penalti Konsisten: BAHAYA (-10 Poin), WASPADA (-2 Poin)
    penalty = (danger_count * 10) + (warning_count * 2)
    safety_score = max(0, 100 - penalty)

    if safety_score >= 85:
        rating = "EXCELLENT"
    elif safety_score >= 70:
        rating = "GOOD"
    elif safety_score >= 50:
        rating = "FAIR"
    else:
        rating = "POOR"

    return {
        "total_events": total_events,
        "danger_count": danger_count,
        "warning_count": warning_count,
        "safety_score": safety_score,
        "rating": rating
    }