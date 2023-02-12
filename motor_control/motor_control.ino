const int stepPin = 5;
const int dirPin = 12;

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  digitalWrite(dirPin, HIGH);
}

unsigned long prev_time = micros();
int step_state_1 = 1;

void loop()
{
  if (micros() - prev_time > 400)
  {
    step_state_1 = !step_state_1;
    digitalWrite(stepPin, step_state_1);
    prev_time = micros();
  }
}
