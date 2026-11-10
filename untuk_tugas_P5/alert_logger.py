import datetime

class AlertLogger:
    def __init__(self):
        self.logs = []

    def log_alert(self, distance, status, speed=None):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Sanitasi status dari karakter newline / control characters
        clean_status = str(status).strip().replace("\n", "").replace("\r", "")
        
        try:
            clean_dist = float(distance)
        except (ValueError, TypeError):
            clean_dist = distance

        if speed is not None:
            try:
                clean_speed = float(speed)
            except (ValueError, TypeError):
                clean_speed = speed
            log_entry = f"[{timestamp}] STATUS: {clean_status} | Jarak: {clean_dist} cm | Kecepatan: {clean_speed} km/h"
        else:
            log_entry = f"[{timestamp}] STATUS: {clean_status} | Jarak: {clean_dist} cm"
            
        self.logs.append(log_entry)
        return log_entry

    def get_logs(self):
        return self.logs