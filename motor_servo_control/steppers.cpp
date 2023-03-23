#include "motor_servo_pinset.h"

// Variables initialaztion for motor 1
int speed_input_1 = 0;
int step_state_1 = 0;
unsigned long prev_time_1 = micros();
int step_delay_1 = 600;

// Variables initialaztion for motor 2
int speed_input_2 = 0;
int step_state_2 = 0;
unsigned long prev_time_2 = micros();
int step_delay_2 = 600;

unsigned long actual_time = micros();

void motors_control()
{
    // Read PWM signal input
    speed_input_1 = analogRead(MOTOR_1_SPEED_INPUT);
    speed_input_2 = analogRead(MOTOR_2_SPEED_INPUT);

    // Set direction motors, inversed due to pullup
    digitalWrite(MOTOR_1_DIRECTION, digitalRead(MOTOR_1_DIRECTION_INPUT));
    digitalWrite(MOTOR_2_DIRECTION, digitalRead(MOTOR_2_DIRECTION_INPUT));

    actual_time = micros();
    
    // Motor 1 control
    if (speed_input_1 > 50 && actual_time - prev_time_1 > step_delay_1)
    {
        prev_time_1 = actual_time;
        step_delay_1 = map(speed_input_1, 10, 1023, 1200, 400);
        digitalWrite(MOTOR_1_STEP, step_state_1);
        step_state_1 = !step_state_1;
    }

    // Motor 2 control
    if (speed_input_2 > 50 && actual_time - prev_time_2 > step_delay_2)
    {
        prev_time_2 = actual_time;
        step_delay_2 = map(speed_input_2, 10, 1023, 1200, 400);
        digitalWrite(MOTOR_2_STEP, step_state_2);
        step_state_2 = !step_state_2;
    }
}