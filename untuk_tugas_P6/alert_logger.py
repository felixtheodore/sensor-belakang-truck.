import datetime

class AlertLogger:
    def __init__(self):
        self.logs = []

    def log_alert(self, distance, status, speed=None):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Sanitasi status dari karakter control/newline
        clean_status = str(status).strip().replace("\n", "").replace("\r", "")
        
        try:
            clean_dist = float(distance)
        except (ValueError, TypeError):
            clean_dist = str(distance).strip().replace("\n", "").replace("\r", "")

        clean_speed = None
        if speed is not None:
            try:
                clean_speed = float(speed)
            except (ValueError, TypeError):
                clean_speed = str(speed).strip().replace("\n", "").replace("\r", "")

        log_entry = {
            "timestamp": timestamp,
            "status": clean_status,
            "distance": clean_dist,
            "speed": clean_speed,
            "formatted": f"[{timestamp}] STATUS: {clean_status} | Jarak: {clean_dist} cm" + (f" | Kecepatan: {clean_speed} km/h" if clean_speed is not None else "")
        }
        
        self.logs.append(log_entry)
        return log_entry["formatted"]

    def log_status(self, distance, status, speed=None):
        return self.log_alert(distance, status, speed)

    def get_logs(self):
        return self.logs

    def count_danger_alerts(self):
        """Menghitung log yang berstatus BAHAYA secara presisi (mencegah penjelajahan substring palsu)."""
        return sum(
            1 for log in self.logs 
            if (isinstance(log, dict) and log.get("status") == "BAHAYA") 
            or (isinstance(log, str) and log == "BAHAYA")
        )

    def clear_logs(self):
        self.logs.clear()


def log_alert(distance, status, speed=None):
    logger = AlertLogger()
    return logger.log_alert(distance, status, speed)

def log_status(distance, status, speed=None):
    logger = AlertLogger()
    return logger.log_status(distance, status, speed)