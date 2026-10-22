import pytest
from buzzer_controller import get_buzzer_config

def test_buzzer_controller_patterns():
    danger_cfg = get_buzzer_config("BAHAYA")
    assert danger_cfg["pattern"] == "FAST_BEEP"
    assert danger_cfg["freq_hz"] == 2000

    warning_cfg = get_buzzer_config("WASPADA")
    assert warning_cfg["pattern"] == "SLOW_BEEP"

    safe_cfg = get_buzzer_config("AMAN")
    assert safe_cfg["pattern"] == "SILENT"

def test_buzzer_controller_invalid_status():
    with pytest.raises(ValueError):
        get_buzzer_config("UNKNOWN_STATUS")