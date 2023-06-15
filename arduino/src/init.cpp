#include "motor_servo_pinset.h"

// Servos variables
Servo servo_1;
Servo servo_2;
int angle_servo_1 = 90;
int angle_servo_2 = 70;

void init_servos()
{
    // Initialize Servo 1 varibles
    servo_1.attach(PIN_SERVO_1);
    servo_1.write(angle_servo_1);
    pinMode(SERVO_1_INCR, INPUT_PULLUP);
    pinMode(SERVO_1_DIR, INPUT_PULLUP);
    // Initialize Servo 2 variables
    servo_2.attach(PIN_SERVO_2);
    servo_2.write(angle_servo_2);
    pinMode(SERVO_2_INCR, INPUT_PULLUP);
    pinMode(SERVO_2_DIR, INPUT_PULLUP);
}

void init_motors()
{
    // Motor 1 GPIO initialization
    pinMode(MOTOR_1_STEP, OUTPUT);
    pinMode(MOTOR_1_DIRECTION, OUTPUT);
    pinMode(MOTOR_1_SPEED_INPUT, INPUT);
    pinMode(MOTOR_1_DIRECTION_INPUT, INPUT_PULLUP);
    digitalWrite(MOTOR_1_STEP, LOW);
    digitalWrite(MOTOR_1_DIRECTION, HIGH);

    // Motor 2 GPIO initialization
    pinMode(MOTOR_2_STEP, OUTPUT);
    pinMode(MOTOR_2_DIRECTION, OUTPUT);
    pinMode(MOTOR_2_SPEED_INPUT, INPUT);
    pinMode(MOTOR_2_DIRECTION_INPUT, INPUT_PULLUP);
    digitalWrite(MOTOR_2_STEP, LOW);
    digitalWrite(MOTOR_2_DIRECTION, HIGH);
}
