import os
from flask import Flask, render_template, request, jsonify
from distance_checker import evaluate_distance
from speed_adjuster import calculate_dynamic_threshold
from alert_logger import AlertLogger
from report_generator import generate_trip_report

app = Flask(__name__)
logger = AlertLogger()

@app.route('/')
@app.route('/sensor-truck')
def index():
    return render_template('index.html')

@app.route('/api/simulate', methods=['POST'])
def simulate():
    data = request.get_json() or {}
    try:
        speed = float(data.get('speed', 8.0))
        distance = float(data.get('distance', 100.0))
        
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
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)