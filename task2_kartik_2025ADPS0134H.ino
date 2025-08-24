int sensorpin = A0;  
int sensor;
int s = 0;  // avg of pressure of t-1
int q = 0;  // avg of pressure at t-2

int led1 = 8;
int led2 = 9;
int led3 = 10;
int led4 = 11;
int led5 = 13;
int piezoPin = 7;

const int WINDOW_SIZE = 3;
double buffer[WINDOW_SIZE] = {0};
int index = 0;
int count = 0;
double sum = 0;

double movingAverage(double newValue) {
  sum -= buffer[index];
  buffer[index] = newValue;
  sum += newValue;
  index = (index + 1) % WINDOW_SIZE;
  if (count < WINDOW_SIZE) count++;
  return sum / count;
}

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(piezoPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  sensor = analogRead(sensorpin);
  double avg = movingAverage(sensor);

  Serial.print("Sensor: ");
  Serial.print(sensor);
  Serial.print(" | Avg: ");
  Serial.println(avg);

  // working of LEDs
  if (avg < s && s < q) {
    digitalWrite(led1, HIGH);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
    digitalWrite(led5, LOW);
  }
  else if (avg == s) {
    digitalWrite(led1, LOW);
    digitalWrite(led2, HIGH);
    digitalWrite(led3, LOW);
    digitalWrite(led5, LOW);
  }
  else if (avg > s && s < q) {
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, HIGH);
    digitalWrite(led5, HIGH);
  }
  else if (avg > s && s > q) {
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, HIGH);
    digitalWrite(led5, LOW);
  }
  //piezo working 
  if (q > s && avg > s) {
    tone(piezoPin, 1000, 300); // 1 kHz for 300 ms
  }

  q = s;
  s = avg;
  delay(100);
}








