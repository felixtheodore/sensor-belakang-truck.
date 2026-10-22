def evaluate_distance(distance_cm: float) -> str:
    if not isinstance(distance_cm, (int, float)):
        raise ValueError("Input jarak harus berupa angka")
    if distance_cm < 0:
        raise ValueError("Jarak tidak boleh bernilai negatif")
        
    if distance_cm > 500:
        return "OUT_OF_RANGE"
    elif distance_cm >= 300:
        return "AMAN"
    elif distance_cm >= 100:
        return "WASPADA"
    else:
        return "BAHAYA"