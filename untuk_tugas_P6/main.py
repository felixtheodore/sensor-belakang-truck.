from distance_checker import evaluate_distance
from speed_adjuster import calculate_dynamic_threshold
from buzzer_controller import get_buzzer_config
from alert_logger import AlertLogger
from report_generator import generate_trip_report

def run_simulation():
    logger = AlertLogger()
    print("=== SENSOR BELAKANG TRUK - MVP VERSION FINAL (P8) ===")

    try:
        speed_input = input("Masukkan kecepatan mundur truk (km/jam) [Default: 8.0]: ").strip()
        speed = float(speed_input) if speed_input else 8.0
        danger_threshold = calculate_dynamic_threshold(100, speed)
        print(f"[CONFIG] Kecepatan: {speed} km/h | Ambang Bahaya Dinamis: {danger_threshold} cm\n")
    except ValueError:
        print("[ERROR] Input kecepatan tidak valid. Menggunakan default 8.0 km/h.\n")
        speed = 8.0
        danger_threshold = 150.0

    # Sampel jarak mencakup titik kritis 120 cm
    sample_distances = [600, 350, 180, 120, 40]
    print("--- MENGUJI SIMULASI JARAK ---")
    for dist in sample_distances:
        try:
            status = evaluate_distance(dist, danger_threshold)
            buzzer = get_buzzer_config(status)
            logger.log_status(dist, status)
            print(f"Jarak: {dist} cm | Status: {status} | Buzzer: {buzzer['pattern']} ({buzzer['freq_hz']} Hz)")
        except ValueError as e:
            print(f"Jarak: {dist} cm | Error: {e}")

    print("\n--- UJI PENANGANAN INPUT INVALID ---")
    for inv in [-10, "abc"]:
        try:
            evaluate_distance(inv)
        except ValueError:
            print(f"Input '{inv}' -> BERHASIL DITOLAK (Handled via Exception)")

    print("\n=== LAPORAN KESELAMATAN PERJALANAN ===")
    report = generate_trip_report(logger.logs)
    print(f"Total Kejadian : {report['total_events']}")
    print(f"Jumlah Bahaya  : {report['danger_count']}")
    print(f"Skor Keamanan  : {report['safety_score']} / 100")
    print(f"Rating Driver  : {report['rating']}")

if __name__ == "__main__":
    run_simulation()