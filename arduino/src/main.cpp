#include "motor_servo_pinset.h"

void setup()
{
    Serial.begin(9600);
    pinMode(LED, OUTPUT);
    digitalWrite(LED, LOW);

    init_servos();
    init_motors();
    init_gyro();
}

void loop()
{
    servo_control();
    motors_control();
}