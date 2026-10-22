from distance_checker import evaluate_distance
from alert_logger import AlertLogger
from speed_adjuster import calculate_dynamic_threshold
from buzzer_controller import get_buzzer_config
from report_generator import generate_trip_report

def main():
    print("=== DEMO MVP VERSION 1 (P6) ===")
    logger = AlertLogger()
    sample_distances = [600, 350, 180, 40]
    speed = 8.0  # km/jam (mundur agak cepat)

    base_danger_limit = 100
    dynamic_limit = calculate_dynamic_threshold(base_danger_limit, speed)
    print(f"[CONFIG] Kecepatan: {speed} km/h | Ambang Bahaya Dinamis: {dynamic_limit} cm\n")

    for dist in sample_distances:
        status = evaluate_distance(dist)
        logger.log_status(dist, status)
        buzzer = get_buzzer_config(status)
        print(f"Jarak: {dist} cm | Status: {status} | Buzzer: {buzzer['pattern']} ({buzzer['freq_hz']} Hz)")

    report = generate_trip_report(logger.logs)
    print("\n=== LAPORAN KESELAMATAN PERJALANAN ===")
    print(f"Total Kejadian : {report['total_events']}")
    print(f"Jumlah Bahaya  : {report['danger_count']}")
    print(f"Skor Keamanan  : {report['safety_score']} / 100")
    print(f"Rating Drivier : {report['rating']}")

if __name__ == "__main__":
    main()