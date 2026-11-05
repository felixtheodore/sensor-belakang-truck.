import math

def calculate_dynamic_threshold(base_threshold=100.0, speed=0.0):
    """
    Menghitung ambang batas bahaya dinamis berdasarkan kecepatan kendaraan.
    Jika kecepatan > 5.0 km/h, ambang bahaya naik dari 100 cm menjadi 150 cm.
    """
    # Validasi input kecepatan (fallback ke 8.0 km/h jika invalid)
    if isinstance(speed, bool) or not isinstance(speed, (int, float)):
        speed = 8.0
    elif math.isnan(speed) or math.isinf(speed) or speed < 0:
        speed = 8.0

    # Validasi base_threshold (fallback ke 100.0 jika invalid)
    if isinstance(base_threshold, bool) or not isinstance(base_threshold, (int, float)):
        base_threshold = 100.0
    elif math.isnan(base_threshold) or math.isinf(base_threshold) or base_threshold < 0:
        base_threshold = 100.0

    if speed > 5.0:
        return float(base_threshold) + 50.0  # 150.0 cm
    return float(base_threshold)            # 100.0 cm