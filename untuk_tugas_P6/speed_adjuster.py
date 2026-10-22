def calculate_dynamic_threshold(base_threshold: float, speed_kmh: float) -> float:
    if not isinstance(speed_kmh, (int, float)) or not isinstance(base_threshold, (int, float)):
        raise ValueError("Kecepatan dan ambang batas harus berupa angka")
    if speed_kmh < 0 or base_threshold < 0:
        raise ValueError("Nilai tidak boleh negatif")
        
    if speed_kmh > 5:
        return base_threshold * 1.5
    return base_threshold * 1.0