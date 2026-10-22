def generate_trip_report(logs: list) -> dict:
    score = 100
    danger_count = sum(1 for log in logs if log.get("status") == "BAHAYA")
    warning_count = sum(1 for log in logs if log.get("status") == "WASPADA")
    
    score -= (danger_count * 10 + warning_count * 2)
    score = max(0, score)
    
    if score >= 80:
        rating = "EXCELLENT"
    elif score >= 60:
        rating = "GOOD"
    else:
        rating = "RISKY"
        
    return {
        "total_events": len(logs),
        "danger_count": danger_count,
        "warning_count": warning_count,
        "safety_score": score,
        "rating": rating
    }