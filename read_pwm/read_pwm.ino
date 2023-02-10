/*
const int stepPin = 3;
const int dirPin = 4;
int del = 500;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  digitalWrite(dirPin, HIGH);
}

void loop() {
  if (Serial.available() > 0)
  {
    del = Serial.readStringUntil(' ').toInt();
  }
  Serial.println(del);
  for(int i=0; i < 200; i++) { // step angle = 1.8, 1 angle each millisecond. 200 ms to a complete cicle
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(del);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(del);
  }
}
*/

const int inpt = A0;
const int otpt = 5;
const int led = 13;
int val, inpt_val = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(otpt, OUTPUT);
  // pinMode(inpt, INPUT);
  pinMode(led, OUTPUT);  
}

void loop()
{
  // analogWrite(otpt, 120);
  val = analogRead(inpt);
  // Serial.println(val);
  analogWrite(led, val / 4);

  // digitalWrite(otpt, LOW);
  // delay(500);
}
