import math

def calculate_dynamic_threshold(base_threshold=100.0, speed=0.0):
    """
    Menghitung ambang batas bahaya dinamis berdasarkan kecepatan kendaraan.
    Melempar ValueError jika input numerik tidak valid, boolean, NaN, Inf, atau negatif.
    """
    if isinstance(speed, bool) or not isinstance(speed, (int, float)):
        raise ValueError("Kecepatan harus berupa angka numerik")
    if math.isnan(speed) or math.isinf(speed):
        raise ValueError("Kecepatan tidak boleh NaN atau Infinity")
    if speed < 0:
        raise ValueError("Kecepatan tidak boleh negatif")

    if isinstance(base_threshold, bool) or not isinstance(base_threshold, (int, float)):
        raise ValueError("Base threshold harus berupa angka numerik")
    if math.isnan(base_threshold) or math.isinf(base_threshold) or base_threshold < 0:
        raise ValueError("Base threshold tidak boleh NaN, Infinity, atau negatif")

    if speed > 5.0:
        return float(base_threshold) + 50.0  # 150.0 cm
    return float(base_threshold)            # 100.0 cm