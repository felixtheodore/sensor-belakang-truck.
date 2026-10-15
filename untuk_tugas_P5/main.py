from distance_checker import evaluate_distance
from alert_logger import AlertLogger

def main():
    print("=== DEMO SIMULASI APLIKASI MVP P5 ===")
    logger = AlertLogger()
    sample_distances = [600, 350, 150, 40, -10]

    for dist in sample_distances:
        try:
            status = evaluate_distance(dist)
            logger.log_status(dist, status)
            print(f"[OK] Jarak: {dist} cm -> Status: {status}")
        except ValueError as e:
            print(f"[ERROR] Jarak: {dist} cm -> {e}")

    print(f"\n[RINGKASAN] Total Deteksi BAHAYA: {logger.count_danger_alerts()}")

if __name__ == "__main__":
    main()