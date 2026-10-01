# Arsitektur Sistem — Sensor Belakang Truk

## 1. Deskripsi

Sensor Belakang Truk adalah alat pendeteksi kendaraan di belakang truk 
berbasis Arduino Uno dan sensor ultrasonic HC-SR04. Alat ini memberikan 
peringatan berupa suara (buzzer) dan cahaya (LED) ketika ada kendaraan 
di belakang truk saat mundur.

## 2. Komponen Sistem

| Komponen | Fungsi |
|----------|--------|
| Arduino Uno R3 | Mikrokontroler utama, memproses data |
| Sensor HC-SR04 | Mendeteksi jarak objek di belakang truk |
| Buzzer aktif | Output suara peringatan |
| LED Merah | Indikator bahaya (jarak < 100 cm) |
| LED Kuning | Indikator waspada (jarak 100-300 cm) |
| LED Hijau | Indikator aman (jarak > 300 cm) |
| Resistor 220Ω | Membatasi arus ke LED |
| Breadboard | Media perakitan rangkaian |
| Kabel jumper | Menghubungkan komponen |

## 3. Diagram Blok Sistem
