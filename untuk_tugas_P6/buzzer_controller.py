def get_buzzer_config(status: str) -> dict:
    valid_statuses = ["AMAN", "WASPADA", "BAHAYA", "OUT_OF_RANGE"]
    if status not in valid_statuses:
        raise ValueError(f"Status tidak valid: {status}")
        
    if status == "BAHAYA":
        return {"freq_hz": 2000, "interval_ms": 100, "pattern": "FAST_BEEP"}
    elif status == "WASPADA":
        return {"freq_hz": 1000, "interval_ms": 500, "pattern": "SLOW_BEEP"}
    else:
        return {"freq_hz": 0, "interval_ms": 0, "pattern": "SILENT"}