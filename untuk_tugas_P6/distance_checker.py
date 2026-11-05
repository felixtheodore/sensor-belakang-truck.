import math

def evaluate_distance(distance, danger_threshold=100.0):
    """
    Menevaluasi status keamanan berdasarkan jarak dan ambang batas bahaya.
    Menolak input non-numerik, boolean, NaN, Inf, dan angka negatif.
    """
    # Tolak tipe boolean (karena di Python bool adalah subclass dari int)
    if isinstance(distance, bool) or not isinstance(distance, (int, float)):
        raise ValueError("Input jarak harus berupa angka numerik (int/float)")
    
    # Tolak NaN dan Infinity
    if math.isnan(distance) or math.isinf(distance):
        raise ValueError("Input jarak tidak boleh NaN atau Infinity")
        
    # Tolak jarak negatif
    if distance < 0:
        raise ValueError("Jarak tidak boleh negatif")

    # Evaluasi logika batas jarak
    if distance > 500:
        return "OUT_OF_RANGE"
    elif distance >= 300:
        return "AMAN"
    elif distance < danger_threshold:
        return "BAHAYA"
    else:
        return "WASPADA"