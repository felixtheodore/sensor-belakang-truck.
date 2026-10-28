def evaluate_distance(distance, danger_threshold=100):
    if not isinstance(distance, (int, float)):
        raise ValueError("Jarak harus berupa angka")
    if distance < 0:
        raise ValueError("Jarak tidak boleh negatif")

    if distance > 500:
        return "OUT_OF_RANGE"
    elif distance >= 300:
        return "AMAN"
    elif distance >= danger_threshold:
        return "WASPADA"
    else:
        return "BAHAYA"