# Arsitektur Sistem — Sensor Belakang Truk

## 1. Deskripsi

Sensor Belakang Truk adalah alat pendeteksi kendaraan di belakang truk berbasis Arduino Uno dan sensor ultrasonic HC-SR04. Alat ini memberikan peringatan berupa suara (buzzer) dan cahaya (LED) ketika ada kendaraan di belakang truk saat mundur.

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

```
┌─────────────────┐
│  Sensor HC-SR04 │
│  (Input)        │
└────────┬────────┘
         │ Sinyal Ultrasonic
         ▼
┌─────────────────┐
│  Arduino Uno R3 │
│  (Proses)       │
└────────┬────────┘
         │
         ├──────────────► Buzzer (Output Suara)
         │
         ├──────────────► LED Merah (Output Visual)
         │
         ├──────────────► LED Kuning (Output Visual)
         │
         └──────────────► LED Hijau (Output Visual)
```

## 4. Arsitektur Perangkat Keras

```
              ┌──────────────────────┐
              │    ARDUINO UNO R3    │
              │                      │
              │  Pin 5V  ────────────┼───► HC-SR04 VCC
              │  Pin 9   ────────────┼───► HC-SR04 TRIG
              │  Pin 10  ────────────┼───► HC-SR04 ECHO
              │  Pin GND ────────────┼───► HC-SR04 GND
              │                      │
              │  Pin 8   ────────────┼───► Buzzer +
              │  Pin GND ────────────┼───► Buzzer −
              │                      │
              │  Pin 7   ────────────┼───► LED Merah
              │  Pin 6   ────────────┼───► LED Kuning
              │  Pin 5   ────────────┼───► LED Hijau
              │  Pin GND ────────────┼───► Semua LED −
              └──────────────────────┘
```

## 5. Arsitektur Perangkat Lunak

```
┌─────────────────────────────────────┐
│         sensor-truck.ino            │
│                                     │
│  ┌───────────────────────────────┐  │
│  │         setup()               │  │
│  │  - Inisialisasi pin           │  │
│  │  - Inisialisasi serial        │  │
│  └───────────────────────────────┘  │
│                                     │
│  ┌───────────────────────────────┐  │
│  │         loop()                │  │
│  │  - Baca sensor                │  │
│  │  - Filter data (median)       │  │
│  │  - Tentukan status bahaya     │  │
│  │  - Aktifkan output            │  │
│  └───────────────────────────────┘  │
│                                     │
│  ┌───────────────────────────────┐  │
│  │     bacaJarak()               │  │
│  │  - Trigger sensor             │  │
│  │  - Hitung durasi pantulan     │  │
│  │  - Konversi ke cm             │  │
│  └───────────────────────────────┘  │
│                                     │
│  ┌───────────────────────────────┐  │
│  │    bacaJarakStabil()          │  │
│  │  - Baca 5x                    │  │
│  │  - Ambil nilai median         │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

## 6. Alur Logika Sistem

```
MULAI
  │
  ▼
Inisialisasi Pin & Serial
  │
  ▼
Baca Sensor HC-SR04 (5x)
  │
  ▼
Hitung Median Jarak
  │
  ▼
Jarak < 100 cm? ─── Ya ──► LED Merah + Buzzer Kencang
  │ Tidak
  ▼
Jarak < 300 cm? ─── Ya ──► LED Kuning + Buzzer Pelan
  │ Tidak
  ▼
LED Hijau + Buzzer Mati
  │
  ▼
Delay 150 ms
  │
  └────► Loop kembali
```

## 7. Spesifikasi Teknis

| Parameter | Nilai |
|-----------|-------|
| Mikrokontroler | ATmega328P (Arduino Uno R3) |
| Tegangan Operasi | 5V DC |
| Sensor | HC-SR04 Ultrasonic |
| Frekuensi Sensor | 40 kHz |
| Jarak Deteksi | 2 cm – 400 cm |
| Sudut Deteksi | 15° |
| Interval Pembacaan | 150 ms |
| Metode Filter | Median dari 5 pembacaan |

## 8. Batasan Sistem

- Sensor HC-SR04 tidak tahan air (perlu casing tambahan).
- Jarak maksimal deteksi 4 meter (bukan 5 meter).
- Sudut deteksi hanya 15° (perlu beberapa sensor untuk cakupan luas).
- Sensitif terhadap getaran dan angin kencang.
- Belum ada fitur IoT atau monitoring jarak jauh.

## 9. Pengembangan Selanjutnya

- [ ] Ganti HC-SR04 dengan JSN-SR04T (waterproof).
- [ ] Tambah sensor di 3 titik (kiri, tengah, kanan).
- [ ] Tambah LCD untuk menampilkan jarak.
- [ ] Integrasi dengan ESP32 untuk monitoring via smartphone.
- [ ] Bikin casing 3D print untuk pemasangan di truk.

## 10. Struktur Repository

```
sensor_truck/
├── readme.md                    # Dokumentasi utama
├── ARCHITECTURE.md              # Dokumen ini
├── sensor-truck.ino             # Kode Arduino
├── flowchart.png                # Diagram alur
└── images/
    ├── tinkercad_bahan.png      # Simulasi Tinkercad
    └── tinkercad-simulasi.png   # Screenshot hasil
```