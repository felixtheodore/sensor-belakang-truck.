import datetime

def log_alert(distance, status, speed=None):
    """
    Mencatat log peringatan dengan sanitasi data numerik dan pencegahan log injection.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Sanitasi string status dari karakter newline / control characters
    clean_status = str(status).strip().replace("\n", "").replace("\r", "")
    
    if speed is not None:
        log_entry = f"[{timestamp}] STATUS: {clean_status} | Jarak: {distance} cm | Kecepatan: {speed} km/h"
    else:
        log_entry = f"[{timestamp}] STATUS: {clean_status} | Jarak: {distance} cm"
        
    return log_entry