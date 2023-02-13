#include "motor_servo_pinset.h"

int read_right_1 = 0;
int read_left_1 = 0;
int read_right_2 = 0;
int read_left_2 = 0;

extern Servo servo_1;
extern Servo servo_2;
extern int angle_servo_1;
extern int angle_servo_2;

int last_check = millis();

void servo_control()
{
    if (millis() - last_check > 500)
    {
        last_check = millis();
        read_right_1 = !digitalRead(SERVO_1_RIGHT);
        read_left_1 = !digitalRead(SERVO_1_LEFT);
        read_right_2 = !digitalRead(SERVO_2_RIGHT);
        read_left_2 = !digitalRead(SERVO_2_LEFT);

        if (read_right_1 || read_left_1 || read_right_2 || read_left_2)
        {
            digitalWrite(LED, HIGH);
            // Servo 1 logic
            if (read_right_1 && modify_angle(&angle_servo_1, delta))
                servo_1.write(angle_servo_1);
            if (read_left_1 && modify_angle(&angle_servo_1, -delta))
                servo_1.write(angle_servo_1);
            // Servo 2 logic
            if (read_right_2 && modify_angle(&angle_servo_2, delta))
                servo_2.write(angle_servo_2);
            if (read_left_2 && modify_angle(&angle_servo_2, -delta))
                servo_2.write(angle_servo_2);
        }
        else
            digitalWrite(LED, LOW);
    }
}

int modify_angle(int *angle, int delta)
{
    *angle += delta;
    if (*angle > 180)
    {
        *angle = 180;
        return (0);
    }
    if (*angle < 0)
    {
        *angle = 0;
        return (0);
    }
    return (1);
}