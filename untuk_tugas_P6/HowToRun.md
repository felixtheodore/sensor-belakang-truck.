# Panduan Menjalankan Aplikasi & Pengujian MVP (P6 - P8)

Dokumen ini berisi panduan teknis langkah demi langkah untuk pengujian fresh clone, eksekusi unit test, audit keamanan, dan penjalankan simulasi CLI.

---

## 🛠️ Prasyarat Sistem
- **Python**: Versi 3.10 atau yang lebih baru.
- **Git**: Untuk proses cloning repositori.
- **Library Python**: `pytest`, `bandit`.

---

## 🚀 Langkah Eksekusi

### 1. Clone Repositori
```bash
git clone [https://github.com/felixtheodore/sensor-belakang-truck.git](https://github.com/felixtheodore/sensor-belakang-truck.git)
cd sensor-belakang-truck
```

### 2. Instalasi Dependensi Pengujian
```bash
py -m pip install pytest bandit
```

### 3. Jalankan Automated Unit Testing (10 Passed)
```bash
cd untuk_tugas_P6
py -m pytest
```

### 4. Jalankan Security Audit
```bash
py -m bandit -r .
```

### 5. Jalankan Simulasi Aplikasi Utama (MVP)
```bash
py main.py
```

---

## 📹 Tautan Video Demo
- **Google Drive Video Demo**: [Tonton Video Demo MVP](https://drive.google.com/file/d/1McnlSCyoNakEchc0a6Rgw_n8VTADnFGz/view?usp=sharing)