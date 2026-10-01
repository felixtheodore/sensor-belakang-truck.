# Sensor Belakang Truk

## Purpose

Alat pendeteksi kendaraan di belakang truk berbasis Arduino Uno dan sensor ultrasonic HC-SR04. Alat ini memberikan peringatan berupa suara (buzzer) dan cahaya (LED) ketika ada mobil atau motor di belakang truk saat mundur. Data jarak diproses secara real-time oleh mikrokontroler dan tidak dikirim ke server manapun.

Tujuan utama: mengurangi risiko kecelakaan akibat blind spot pada truk container.

## Use This Stack

**Hardware:**

* Mikrokontroler: Arduino Uno R3
* Sensor: Ultrasonic HC-SR04
* Output Suara: Buzzer aktif 5V
* Output Visual: LED Merah, Kuning, Hijau
* Resistor: 220Ω (3 buah)
* Media Rakit: Breadboard + kabel jumper

**Software:**

* Bahasa: C++ (Arduino)
* IDE: Arduino IDE 2.x
* Simulasi: Tinkercad Circuits
* Version Control: Git + GitHub
* Dokumentasi: Markdown

## Code Rules

* Do not add comments unless truly necessary.
* Gunakan `PascalCase` untuk nama fungsi utama (contoh: `BacaJarakStabil`).
* Local variables gunakan `camelCase` (contoh: `jarakSekarang`).
* Nama konstanta gunakan `UPPER_SNAKE_CASE` (contoh: `BATAS_BAHAYA`).
* Keep code lines below 150 characters where practical.
* Satu file utama: `sensor-truck.ino`.
* Hindari `delay()` panjang yang memblokir pembacaan sensor.
* Gunakan filter median untuk stabilkan pembacaan sensor.

## Main Components

1. Sensor

   * Id
   * Nama
   * PinTrig
   * PinEcho
   * JarakMaksimal
   * Frekuensi
   * SudutDeteksi

2. Aktuator

   * Id
   * Nama
   * Pin
   * Tipe
   * StatusAktif

3. Indikator

   * Id
   * Warna
   * Pin
   * Resistor
   * KondisiNyala

4. Pembacaan

   * Id
   * Timestamp
   * JarakCm
   * StatusBahaya
   * NilaiMedian
   * JumlahSample

## Logic Rules

* Pembacaan sensor dilakukan minimal 5x berturut-turut sebelum diambil nilai median.
* Nilai `-1` berarti sensor tidak mendeteksi objek (dianggap aman).
* Jarak di atas 500 cm dianggap tidak ada objek.
* Nilai ambang batas tidak boleh diubah saat runtime.
* Status bahaya hanya boleh satu aktif pada satu waktu.
* Delay antar loop maksimal 150 ms agar responsif.
* Tidak ada penyimpanan data ke memori permanen (EEPROM/SD card) di versi pertama.

## Main Features

1. Deteksi Jarak

   * Baca jarak objek di belakang truk secara real-time.
   * Range deteksi: 2 cm – 400 cm.

2. Klasifikasi Bahaya

   * Aman: jarak > 300 cm
   * Waspada: jarak 100–300 cm
   * Bahaya: jarak < 100 cm

3. Output Suara

   * Buzzer mati saat aman.
   * Buzzer pelan (1000 Hz) saat waspada.
   * Buzzer kencang (2000 Hz) saat bahaya.

4. Output Visual

   * LED Hijau menyala saat aman.
   * LED Kuning menyala saat waspada.
   * LED Merah menyala saat bahaya.

5. Filter Data

   * Median dari 5 pembacaan terakhir.
   * Abaikan pembacaan tidak valid (durasi 0).

## Operating Modes

1. Mode Normal

   * Alat menyala, sensor membaca terus-menerus.
   * Output menyesuaikan jarak objek.

2. Mode Idle

   * Tidak ada objek terdeteksi.
   * LED Hijau menyala, buzzer mati.

3. Mode Waspada

   * Objek terdeteksi pada 100–300 cm.
   * LED Kuning menyala, buzzer pelan.

4. Mode Bahaya

   * Objek terdeteksi < 100 cm.
   * LED Merah menyala, buzzer kencang.

5. Mode Error

   * Sensor tidak merespons (durasi = 0).
   * LED Hijau menyala, buzzer mati (fail-safe).

## Hardware Requirements

* Tegangan operasi sistem: 5V DC.
* Sumber daya: adaptor 5V atau step-down dari aki truk 12V → 5V.
* Konsumsi daya maksimal: 500 mA.
* Casing sensor: minimal IP54 (tahan debu & cipratan air).
* Kabel: jumper male-female 20 cm.
* Semua sambungan harus disolder atau dikunci dengan konektor, tidak boleh longgar.
* LED wajib dilindungi resistor 220Ω.
* Sensor dipasang di bumper belakang, menghadap ke bawah 10–15°.

## Required Pin Mapping

* HC-SR04 VCC → Arduino 5V
* HC-SR04 TRIG → Arduino Pin 9
* HC-SR04 ECHO → Arduino Pin 10
* HC-SR04 GND → Arduino GND
* Buzzer Positif → Arduino Pin 8
* Buzzer Negatif → Arduino GND
* LED Merah Anoda → Arduino Pin 7 (via resistor 220Ω)
* LED Merah Katoda → Arduino GND
* LED Kuning Anoda → Arduino Pin 6 (via resistor 220Ω)
* LED Kuning Katoda → Arduino GND
* LED Hijau Anoda → Arduino Pin 5 (via resistor 220Ω)
* LED Hijau Katoda → Arduino GND

## Deliverables

* Source code lengkap (`sensor-truck.ino`).
* Flowchart logika sistem.
* Dokumen arsitektur (file ini).
* Diagram blok sistem.
* Diagram wiring / pin mapping.
* Simulasi Tinkercad (screenshot atau link).
* README berisi cara install, cara upload, cara pakai, dan dokumentasi komponen.
* Alat sudah diuji dan berfungsi sesuai spesifikasi.

## Project Structure

```text
sensor_truck/
  sensor-truck.ino
  readme.md
  ARCHITECTURE.md
  flowchart.png
  images/
    tinkercad-simulasi.png
    tinkercad-bahan.png
    wiring.png
```

## Code Modules

* `setup()`

  * Inisialisasi pin input/output.
  * Inisialisasi Serial Monitor (9600 baud).
  * Cetak pesan "Sensor Mundur Truk Siap".

* `loop()`

  * Baca sensor dengan filter median.
  * Klasifikasi status bahaya.
  * Aktifkan output (LED + buzzer).
  * Delay 150 ms.

* `BacaJarak()`

  * Trigger sensor HC-SR04.
  * Hitung durasi pantulan.
  * Konversi ke cm.
  * Return `-1` jika tidak ada pantulan.

* `BacaJarakStabil()`

  * Panggil `BacaJarak()` 5 kali.
  * Buang nilai tidak valid.
  * Urutkan dan ambil median.
  * Return nilai median.

* `MatikanSemuaLed()`

  * Reset semua LED ke kondisi LOW.
  * Digunakan sebelum menyalakan LED baru.

## Model Rules

* Semua pin didefinisikan sebagai `const int` di awal file.
* Nilai ambang batas didefinisikan sebagai `const long`.
* Tidak boleh ada magic number di dalam `loop()` atau fungsi lain.
* Tidak boleh ada duplikasi logika pembacaan sensor.
* Fungsi harus punya satu tanggung jawab (single responsibility).
* Nama variabel dan fungsi harus deskriptif (bukan `x`, `y`, `temp`).
* Kode harus bisa dikompilasi tanpa warning di Arduino IDE.