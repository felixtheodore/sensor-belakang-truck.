class AlertLogger:
    def __init__(self):
        self.logs = []

    def log_status(self, distance_cm: float, status: str) -> dict:
        entry = {"distance": distance_cm, "status": status}
        self.logs.append(entry)
        return entry

    def count_danger_alerts(self) -> int:
        return sum(1 for log in self.logs if log["status"] == "BAHAYA")