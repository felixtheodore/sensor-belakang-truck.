// Smart Rear-Truck Obstacle & Safety Monitoring System (Arduino Firmware)
// Hardware Proof of Concept (Fail-Safe Implementation)

const int TRIG_PIN = 9;
const int ECHO_PIN = 10;
const int LED_MERAH = 7;   // Selaras dengan ARCHITECTURE.md
const int LED_KUNING = 6;  // Selaras dengan ARCHITECTURE.md
const int LED_HIJAU = 5;   // Selaras dengan ARCHITECTURE.md
const int BUZZER = 8;      // Selaras dengan ARCHITECTURE.md

void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(LED_MERAH, OUTPUT);
  pinMode(LED_KUNING, OUTPUT);
  pinMode(LED_HIJAU, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  Serial.begin(9600);
}

long readDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  
  long duration = pulseIn(ECHO_PIN, HIGH, 30000); // Timeout 30ms (~500cm)
  if (duration == 0) {
    return -1; // Sensor timeout / gagal baca
  }
  return duration * 0.034 / 2; // Konversi ke cm
}

void loop() {
  long jarak = readDistance();
  
  Serial.print("Jarak Terukur: ");
  Serial.print(jarak);
  Serial.println(" cm");

  // Proteksi Fail-Safe & Penanganan Logika Jarak
  if (jarak <= 0) {
    // SENSOR ERROR / TIMEOUT -> FAIL-SAFE KE STATUS BAHAYA!
    digitalWrite(LED_MERAH, HIGH);
    digitalWrite(LED_KUNING, LOW);
    digitalWrite(LED_HIJAU, LOW);
    tone(BUZZER, 2000);
  } else if (jarak < 100) {
    // ZONA BAHAYA (< 100 cm)
    digitalWrite(LED_MERAH, HIGH);
    digitalWrite(LED_KUNING, LOW);
    digitalWrite(LED_HIJAU, LOW);
    tone(BUZZER, 2000);
  } else if (jarak < 300) {
    // ZONA WASPADA (100 cm - 299 cm)
    digitalWrite(LED_MERAH, LOW);
    digitalWrite(LED_KUNING, HIGH);
    digitalWrite(LED_HIJAU, LOW);
    tone(BUZZER, 1000);
  } else {
    // ZONA AMAN (>= 300 cm)
    digitalWrite(LED_MERAH, LOW);
    digitalWrite(LED_KUNING, LOW);
    digitalWrite(LED_HIJAU, HIGH);
    noTone(BUZZER);
  }

  delay(150); // Delay 150 ms selaras dengan spesifikasi arsitektur
}