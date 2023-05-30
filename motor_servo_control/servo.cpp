#include "motor_servo_pinset.h"

extern Servo servo_1;
extern Servo servo_2;
extern int angle_servo_1;
extern int angle_servo_2;

int last_read_incr_1 = 1;
int last_read_incr_2 = 1;

int read_incr_1 = 0;
int read_dir_1 = 1;
int read_incr_2 = 0;
int read_dir_2 = 1;

int blink_time = millis();


void servo_control()
{
    read_incr_1 = !digitalRead(SERVO_1_INCR);
    read_dir_1 = !digitalRead(SERVO_1_DIR);
    read_incr_2 = !digitalRead(SERVO_2_INCR);
    read_dir_2 = !digitalRead(SERVO_2_DIR);

    if (read_incr_1 && !last_read_incr_1)
    {
        blinkLed(millis());
        if (read_dir_1)
            modify_angle(&angle_servo_1, -delta_x);
        else
            modify_angle(&angle_servo_1, delta_x);
        servo_1.write(angle_servo_1);
        Serial.println(angle_servo_1);
    }

    if (read_incr_2 && !last_read_incr_2)
    {
        blinkLed(millis());
        if (read_dir_2)
            modify_angle(&angle_servo_2, -delta_y);
        else
            modify_angle(&angle_servo_2, delta_y);
        servo_2.write(angle_servo_2);
        Serial.println(angle_servo_2);
    }

    last_read_incr_1 = read_incr_1;
    last_read_incr_2 = read_incr_2;
    blinkLed(0);
}


void modify_angle(int *angle, int delta)
{
    *angle += delta;
    if (*angle > 180)
    {
        *angle = 180;
        return;
    }
    if (*angle < 0)
    {
        *angle = 0;
        return;
    }
    return;
}


void blinkLed(int t)
{
    if ((!t && millis() > blink_time + 1000) || !blink_time)
    {
        blink_time = 0;
        digitalWrite(LED, LOW);
    }
    if (t)
    {
        digitalWrite(LED, HIGH);
        blink_time = t;
    }
}
