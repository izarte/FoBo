#include "motor_servo_pinset.h"

void setup()
{
    Serial.begin(115200);
    pinMode(LED, OUTPUT);
    digitalWrite(LED, LOW);

    init_servos();
    init_motors();
}

void loop()
{
    servo_control();
    motors_control();
}