# Sensor Belakang Truk

Alat pendeteksi kendaraan di belakang truk menggunakan sensor 

## 📌 Deskripsi

Sensor Belakang Truk merupakan alat yang dibuat untuk membantu sopir truk 
mengetahui keberadaan mobil atau motor di belakang truk saat mundur. 
Alat ini menggunakan sensor ultrasonic HC-SR04 untuk mendeteksi objek 
dan memberikan peringatan berupa buzzer serta LED indikator.

Truk container merupakan kendaraan dengan titik buta (blind spot) terbesar 
di bagian belakang. Oleh karena itu, alat ini dirancang untuk mengurangi 
risiko kecelakaan saat truk mundur.

## 🎯 Tujuan

- Membantu sopir truk mengetahui keberadaan kendaraan di belakang saat mundur.
- Memberikan peringatan dini berupa suara dan cahaya.
- Mengurangi risiko kecelakaan akibat blind spot.
- Meningkatkan keamanan berkendara truk.

## 💡 Manfaat

**Bagi Sopir Truk**
- Mengetahui keberadaan kendaraan di belakang.
- Mendapat peringatan saat akan mundur.
- Mengurangi risiko kecelakaan lalulintas.
  
**Bagi Pengguna Jalan Lain**
- Lebih aman berada di sekitar truk.
- Mengurangi risiko tertabrak saat truk mundur.
- membantu pengendara lebih waspada saat berkendara.
## ⚙️ Komponen

| Komponen | Jumlah |
|----------|--------|
| Arduino Uno R3 | 1 |
| Sensor Ultrasonic HC-SR04 | 1 |
| Buzzer aktif | 1 |
| LED Merah | 1 |
| LED Kuning | 1 |
| LED Hijau | 1 |
| Resistor 220Ω | 3 |
| Kabel jumper | secukupnya |
| Breadboard | 1 |

## 🔄 Cara Kerja

1. Sensor HC-SR04 memancarkan gelombang ultrasonic ke belakang truk.
2. Gelombang akan memantul jika mengenai objek (mobil/motor).
3. Arduino menghitung jarak berdasarkan waktu pantulan gelombang.
4. Alarm berbunyi sesuai tingkat bahaya.

## 🚦 Tingkat Bahaya

| Jarak | Status | LED | Buzzer |
|-------|--------|-----|--------|
| > 300 cm | Aman | Hijau | Mati |
| 100 - 300 cm | Waspada | Kuning | Pelan |
| < 100 cm | Bahaya | Merah | Kencang |

## 🔌 Wiring

| Komponen | Pin Arduino |
|----------|-------------|
| HC-SR04 VCC | 5V |
| HC-SR04 TRIG | 9 |
| HC-SR04 ECHO | 10 |
| HC-SR04 GND | GND |
| Buzzer + | 8 |
| LED Merah | 7 |
| LED Kuning | 6 |
| LED Hijau | 5 |

## 📁 Struktur File

- `sensor-truk.ino` — kode utama Arduino
- `flowchart.png` — diagram alur logika
- `images/` — foto komponen & dokumentasi

## 🚀 Cara Menjalankan

1. Buka Arduino IDE.
2. Paste kode dari `sensor-truk.ino`.
3. Sambungkan Arduino ke laptop menggunakan kabel USB.
4. Pilih Board: **Arduino Uno**.
5. Pilih Port: **COMx** (sesuai yang terdeteksi).
6. Klik tombol **Upload**.

## 📊 Status Project

Status: 🚧 Dalam Pengembangan

- [x] Desain logika & flowchart
- [x] Kode program
- [ ] Rakit hardware
- [ ] Pengujian alat

## 👤 Author

**Nama:** [Felix Theodore]  
**NIM:** [2510101010]  
**Mata Kuliah:** [Rekayasa perangkat lunak]
