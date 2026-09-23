sensor-belakang-truck.
sensor untuk belakang truck adalah sensor yang dibuat untuk keamanan truck yaitu
Alat pendeteksi kendaraan di belakang truk menggunakan sensor ultrasonic HC-SR04.

alasan saya membuat ini (saya tahu sampai sekarang truck container adalah kendaraan dengan titik buta terbesar di belakang
oleh karena itu saya merancang sensor belakang truck ini.
Tujuan
Membantu sopir truk mengetahui keberadaan mobil/motor di belakang saat mundur, 
dengan alarm berupa buzzer dan LED indikator saya berharap alat ini nantinya akan membantu pengendara truck berkendara lebih aman.

Komponen
- Arduino Uno R3
- Sensor Ultrasonic HC-SR04
- Buzzer aktif
- LED (merah, kuning, hijau)
- Resistor 220Ω
- Kabel jumper
- Breadboard

Cara Kerja
1. Sensor HC-SR04 memancarkan gelombang ultrasonic ke belakang truk
2. Gelombang memantul jika ada objek
3. Arduino menghitung jarak berdasarkan waktu pantulan
4. Alarm berbunyi sesuai tingkat bahaya:
   - Jarak > 300 cm Aman (LED hijau, buzzer mati)
   - Jarak 100-300 cm Waspada (LED kuning, buzzer pelan)
   - Jarak < 100 cm Bahaya (LED merah, buzzer kencang)
