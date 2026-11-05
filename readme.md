# Smart Rear-Truck Obstacle & Safety Monitoring System

Sistem pemantauan jarak dan keselamatan objek belakang truk dengan penyesualian ambang batas bahaya secara dinamis berdasarkan kecepatan mundur kendaraan.

---

## 👤 Informasi Mahasiswa & Proyek
- **Nama:** Felix Theodore
- **NIM:** 2510101010
- **Mata Kuliah:** Rekayasa Perangkat Lunak (Pertemuan 8 - Final MVP)
- **Repository:** `sensor-belakang-truck`

---

## 📌 1. Gambaran Umum Proyek (P1 - P7)

### Deskripsi Proyek
Truk kontainer memiliki area *blind spot* terbesar di bagian belakang. Sistem ini dirancang untuk membantu pengemudi truk mendeteksi keberadaan kendaraan/objek di belakang saat mundur menggunakan sensor ultrasonik serta memberikan peringatan dini berupa indikator LED dan Buzzer.

### Tujuan & Manfaat
- **Sopir Truk:** Membantu mengetahui keberadaan kendaraan di area *blind spot* dan mengurangi risiko kecelakaan saat mundur.
- **Pengguna Jalan:** Meningkatkan keselamatan kendaraan lain di sekitar area belakang truk.

### Perangkat Hardware & Komponen
| Komponen | Jumlah | Fungsi / Deskripsi |
| :--- | :--- | :--- |
| Arduino Uno R3 | 1 | Mikrokontroler utama |
| Sensor Ultrasonic HC-SR04 | 1 | Mengukur jarak objek di belakang truk |
| Buzzer Aktif | 1 | Alarm peringatan suara (*beep*) |
| LED Merah, Kuning, Hijau | @1 | Indikator visual status keamanan |
| Resistor 220Ω & Jumper | Secukupnya | Rangkaian pendukung |

### Aturan Bisnis MVP & Ambang Batas Dinamis
- **Jarak > 500 cm**: `OUT_OF_RANGE`
- **Jarak 300 - 500 cm**: `AMAN` (LED Hijau / Buzzer Silent)
- **Kecepatan <= 5 km/h**: Ambang batas bahaya standar = `100 cm`
- **Kecepatan > 5 km/h**: Ambang batas bahaya dinamis naik = `150 cm`
- **Zona Peringatan**:
  - `Jarak < Dynamic Danger Threshold` $\rightarrow$ **BAHAYA** (LED Merah / Fast Beep)
  - `Dynamic Danger Threshold <= Jarak <= 300 cm` $\rightarrow$ **WASPADA** (LED Kuning / Slow Beep)

---

## 🔐 2. Hasil Uji Security & Catatan Perubahan (P8 - Poin 01)

### Laporan Security Audit (Bandit Static Analyzer)
Pengujian keamanan berbasis *Static Application Security Testing* (SAST) telah dijalankan menggunakan **Bandit**:
- **High Severity**: 0
- **Medium Severity**: 0
- **Low Severity**: 23 (Terbatas pada pemakaian `assert` di modul unit test `pytest`, **0 vulnerability** pada kode produksi).

### Catatan Keamanan Kode (Security Fixes):
1. **Validasi Type & Range**: Fungsi `evaluate_distance()` menolak string dan angka negatif via `ValueError` untuk mencegah *unhandled exception*.
2. **Sanitasi Log**: Log sistem hanya mencatat nilai numerik (jarak/kecepatan) tanpa menyimpan *path* sistem internal atau data sensitif.
3. **No Hardcoded Secrets**: Bebas dari penulisan *API Key*, token, atau *credential* di dalam berkas kode.

---

## 🚀 3. Panduan Fresh Clone, Build, & Execution (P8 - Poin 02 & 04)

Panduan pengujian dari nol (*fresh clone*) untuk dosen / asisten laboratorium:

### Langkah 1: Clone Repositori
```bash
git clone https://github.com/felixtheodore/sensor-belakang-truck.git
cd sensor-belakang-truck
```

### Langkah 2: Instalasi Dependensi Pengujian
```bash
py -m pip install pytest bandit
```

### Langkah 3: Jalankan Automated Unit Testing (10 Passed 100%)
```bash
cd untuk_tugas_P6
py -m pytest
```

### Langkah 4: Jalankan Aplikasi Utama (MVP)
```bash
py main.py
```

---

## 📹 4. Tautan Video Demo & Dokumentasi Pendukung

- 📹 **Link Video Demo Google Drive**: [Tonton Video Demo MVP (Google Drive)](https://drive.google.com/file/d/1McnlSCyoNakEchc0a6Rgw_n8VTADnFGz/view)
- 📖 **Panduan Teknis & Akses Demo**: [`untuk_tugas_P6/HowToRun.md`](https://github.com/felixtheodore/sensor-belakang-truck./blob/master/untuk_tugas_P6/HowToRun.md)
- 📋 **MVP Checklist Status**: [`untuk_tugas_P6/checklist_mvp.md`](https://github.com/felixtheodore/sensor-belakang-truck./blob/master/untuk_tugas_P6/checklist_mvp.md)

---

## 🛡️ 5. Contoh Log Aman, Error Handling, & Remediasi (P8 - Poin 03)

| Kategori | Contoh Output / Log Terminal | Penyebab Utama | Tindakan Perbaikan (Remediation) |
| :--- | :--- | :--- | :--- |
| **Normal Log** | `[CONFIG] Kecepatan: 8.0 km/h \| Ambang Bahaya Dinamis: 150.0 cm` | - | Log aman, hanya menampilkan variabel fungsional tanpa informasi sensitif. |
| **Input Invalid (String)** | `Input 'abc' -> BERHASIL DITOLAK (Handled via Exception)` | Pengguna memasukkan karakter non-angka saat input kecepatan/jarak. | Ditangkap oleh `try-except ValueError`, dialihkan ke kecepatan default `8.0 km/h` tanpa membuat aplikasi *crash*. |
| **Input Invalid (Negatif)**| `Input '-10' -> BERHASIL DITOLAK (Handled via Exception)` | Nilai jarak bernilai < 0. | Divalidasi langsung oleh `distance_checker.py` dengan melempar `ValueError("Jarak tidak boleh negatif")`. |
| **Data Log Kosong** | `Rating Driver : EXCELLENT (NO DATA)` | Sistem dipanggil membuat rekap laporan saat riwayat kejadian masih kosong. | `report_generator.py` menangani kondisi array kosong dan mengembalikan skor default 100 secara aman. |