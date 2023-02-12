const int MOTOR_1_STEP = 5;
const int MOTOR_1_DIRECTION = 12;
const int MOTOR_1_SPEED_INPUT = A0;
const int MOTOR_1_DIRECTION_INPUT = A1;
const int LED = 13;

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(MOTOR_1_STEP, OUTPUT);
  pinMode(MOTOR_1_DIRECTION, OUTPUT);
  pinMode(MOTOR_1_SPEED_INPUT, INPUT);
  digitalWrite(MOTOR_1_DIRECTION, HIGH);
  pinMode(LED, OUTPUT);
}

int speed_input_1 = 0;
int step_state_1 = 0;
unsigned long prev_time = millis();
int step_delay = 600;

void loop()
{
  speed_input_1 = analogRead(MOTOR_1_SPEED_INPUT);
  analogWrite(LED, speed_input_1 / 4);
  if (speed_input_1 > 10 && micros() - prev_time > step_delay)
  {
    prev_time = micros();
    step_delay = map(speed_input_1, 10, 1023, 1200, 400);
    digitalWrite(MOTOR_1_STEP, step_state_1);
    step_state_1 = !step_state_1;
  }
}