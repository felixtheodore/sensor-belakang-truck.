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

    def log_status(self, distance, status, speed=None):
        """Alias log_status untuk kompatibilitas test."""
        return self.log_alert(distance, status, speed)

    def get_logs(self):
        """Mengembalikan seluruh riwayat log."""
        return self.logs

    def count_danger_alerts(self):
        """Menghitung jumlah peringatan berstatus BAHAYA."""
        return sum(1 for log in self.logs if "BAHAYA" in log)

    def clear_logs(self):
        """Mengosongkan daftar log."""
        self.logs.clear()

    def get_danger_count(self):
        """Alias keamanan jika test memanggil get_danger_count."""
        return self.count_danger_alerts()


# Wrapper fungsi modular tingkat modul
def log_alert(distance, status, speed=None):
    logger = AlertLogger()
    return logger.log_alert(distance, status, speed)

def log_status(distance, status, speed=None):
    logger = AlertLogger()
    return logger.log_status(distance, status, speed)