const int PinTrig = 9;
const int PinEcho = 10;
const int PinBuzzer = 8;
const int PinLedMerah = 7;
const int PinLedKuning = 6;
const int PinLedHijau = 5;

const long BatasBahaya = 100;
const long BatasWaspada = 300;
const long BatasAman = 500;

long bacaJarak() 
{digitalWrite(PinTrig, LOW);
  delayMicroseconds(2);
  digitalWrite(PinTrig, HIGH);
  delayMicroseconds(10);
  digitalWrite(PinTrig, LOW);

  long durasi = pulseIn(PinEcho, HIGH, 30000);
  if (durasi == 0) 
  {return -1;}

  long jarak = durasi * 0.034 / 2;
  return jarak;}

long bacaJarakStabil() 
{long data[5];
  int jumlahValid = 0;

  for (int i = 0; i < 5; i++) 
  {long j = bacaJarak();
    if (j > 0) {
      data[jumlahValid] = j;
      jumlahValid++;}
    delay(30);}

  if (jumlahValid == 0) {return -1;}

  for (int i = 0; i < jumlahValid - 1; i++) {
    for (int k = 0; k < jumlahValid - i - 1; k++) {
      if (data[k] > data[k + 1]) {
        long tmp = data[k];
        data[k] = data[k + 1];
        data[k + 1] = tmp;}}}

  return data[jumlahValid / 2];}

void matikanSemuaLed() 
{digitalWrite(PinLedMerah, LOW);
  digitalWrite(PinLedKuning, LOW);
  digitalWrite(PinLedHijau, LOW);}

void setup() 
{pinMode(PinTrig, OUTPUT);
  pinMode(PinEcho, INPUT);
  pinMode(PinBuzzer, OUTPUT);
  pinMode(PinLedMerah, OUTPUT);
  pinMode(PinLedKuning, OUTPUT);
  pinMode(PinLedHijau, OUTPUT);

  Serial.begin(9600);
  Serial.println("Sensor Mundur Truk Siap");}

void loop()
{long jarak = bacaJarakStabil();

  Serial.print("Jarak: ");
  if (jarak < 0) 
  {Serial.println("Tidak Terdeteksi");} 
  else {Serial.print(jarak);
    Serial.println(" cm");}

  if (jarak < 0 || jarak > BatasAman) 
  {matikanSemuaLed();
    digitalWrite(PinLedHijau, HIGH);
    noTone(PinBuzzer);
  } else if (jarak < BatasBahaya) {
    matikanSemuaLed();
    digitalWrite(PinLedMerah, HIGH);
    tone(PinBuzzer, 2000);
  } else if (jarak < BatasWaspada) {
    matikanSemuaLed();
    digitalWrite(PinLedKuning, HIGH);
    tone(PinBuzzer, 1000);
  } else {
    matikanSemuaLed();
    digitalWrite(PinLedHijau, HIGH);
    noTone(PinBuzzer);
  }

  delay(150);
}