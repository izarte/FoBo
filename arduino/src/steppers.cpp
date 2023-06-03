#include "motor_servo_pinset.h"

// Variables initialaztion for motor 1
int speed_input_1 = 0;
int step_state_1 = 0;
unsigned long prev_time_1 = micros();
unsigned long step_delay_1 = 600;

// Variables initialaztion for motor 2
int speed_input_2 = 0;
int step_state_2 = 0;
unsigned long prev_time_2 = micros();
unsigned long step_delay_2 = 600;

unsigned long actual_time = micros();
extern float yaw;

extern double Setpoint, Input, Output;
extern PID movement_PID;

float objective = 0.0;
bool goal_seted = false;

void motors_control()
{
    // Read gyro data
    Serial.print("\t");
    Serial.println(Output);

    // Read PWM signal input
    speed_input_1 = analogRead(MOTOR_1_SPEED_INPUT);
    speed_input_2 = analogRead(MOTOR_2_SPEED_INPUT);

    // Set direction motors, inversed due to pullup
    digitalWrite(MOTOR_1_DIRECTION, digitalRead(MOTOR_1_DIRECTION_INPUT));
    digitalWrite(MOTOR_2_DIRECTION, digitalRead(MOTOR_2_DIRECTION_INPUT));

    if (!goal_seted && speed_input_1 == speed_input_2)
    {
        read_yaw();
        Setpoint = yaw;
        goal_seted = true;
    }
    else
        goal_seted = false;

    if (goal_seted)
    {
        read_yaw();
        Input = -abs(yaw);
        movement_PID.Compute();
        Output *= (yaw / abs(yaw));
        speed_input_1 = checkLimits((speed_input_1 - Output), 0, 1023); 
        speed_input_2 = checkLimits((speed_input_2 + Output), 0, 1023); 
    }

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

int checkLimits(int value, int min, int max)
{
    if (value < min)
        return (min);
    if (value > max)
        return (max);
    return (value);
}

// // variables internas del controlador
// unsigned long current_time, prev_time = millis();
// double elapsed_time;
// double error = 0.0, last_error = 0.0, cum_error = 0.0, rate_error = 0.0;

// void PID()
// {
//     current_time = millis();
//     elapsed_time = (double)(current_time - prev_time);
//     error = objective - yaw;
//     cum_error = error * elapsed_time;
//     rate_error = (error - last_error) / elapsed_time;

//     double output = KP * error + KI * cum_error + KD * rate_error;

//     last_error = error;
//     prev_time = current_time;
//     return (output);
// }