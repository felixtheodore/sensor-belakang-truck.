from alert_logger import AlertLogger

def test_alert_logger_recording_and_counting():
    logger = AlertLogger()
    logger.log_status(400, "AMAN")
    logger.log_status(50, "BAHAYA")
    logger.log_status(30, "BAHAYA")

    assert len(logger.logs) == 3
    assert logger.count_danger_alerts() == 2