import math
import os
from flask import Flask, render_template, request, jsonify
from distance_checker import evaluate_distance
from speed_adjuster import calculate_dynamic_threshold
from alert_logger import AlertLogger
from report_generator import generate_trip_report

app = Flask(__name__)

# Gunakan absolute path agar lokasi file log tidak bergantung pada working directory server
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE_PATH = os.path.join(BASE_DIR, 'alert_logs.json')
logger = AlertLogger(log_file=LOG_FILE_PATH)

MAX_SPEED_KMH = 120.0
MAX_DISTANCE_CM = 10000.0

@app.route('/')
@app.route('/sensor-truck')
def index():
    logs = logger.get_logs()
    logs_text = "\n".join(l.get("formatted", str(l)) for l in logs) if logs else "Belum ada simulasi dijalankan..."
    return render_template('index.html', logs_text=logs_text)

@app.route('/api/simulate', methods=['POST'])
def simulate():
    data = request.get_json(silent=True) or {}
    try:
        raw_speed = data.get('speed')
        raw_distance = data.get('distance')

        if raw_speed is None or raw_distance is None or str(raw_speed).strip() == "" or str(raw_distance).strip() == "":
            raise ValueError("Kecepatan dan jarak tidak boleh kosong.")

        speed = float(raw_speed)
        distance = float(raw_distance)

        # Tolak nilai khusus float (NaN / Infinity)
        if math.isnan(speed) or math.isinf(speed) or math.isnan(distance) or math.isinf(distance):
            raise ValueError("Input tidak boleh berupa NaN atau Infinity.")

        # Tolak nilai negatif
        if speed < 0 or distance < 0:
            raise ValueError("Kecepatan dan jarak tidak boleh bernilai negatif.")

        # Tolak nilai melebihi batas wajar maksimal
        if speed > MAX_SPEED_KMH or distance > MAX_DISTANCE_CM:
            raise ValueError(f"Kecepatan maksimal {int(MAX_SPEED_KMH)} km/h dan jarak maksimal {int(MAX_DISTANCE_CM)} cm.")
        
        # Hitung ambang batas dinamis & evaluasi status jarak
        threshold = calculate_dynamic_threshold(100.0, speed)
        status = evaluate_distance(distance, threshold)
        
        # Catat log ke AlertLogger
        logger.log_alert(distance, status, speed)
        logs = logger.get_logs()
        
        # Hitung ringkasan laporan & skor driver
        report = generate_trip_report(logs)
        
        # Tentukan frekuensi buzzer
        buzzer_freq = "0 Hz (SILENT)"
        if status == "BAHAYA":
            buzzer_freq = "2000 Hz (FAST BEEP)"
        elif status == "WASPADA":
            buzzer_freq = "1000 Hz (SLOW BEEP)"

        return jsonify({
            "success": True,
            "status": status,
            "threshold": threshold,
            "buzzer": buzzer_freq,
            "logs": logs,
            "report": report
        })
    except (ValueError, TypeError) as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": "Terjadi kesalahan pada server: " + str(e)}), 500

@app.route('/api/logs/clear', methods=['POST'])
def clear_logs():
    logger.clear_logs()
    return jsonify({"success": True, "logs": []})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)