#include <Servo.h>

const int LED = 13;
// Servo 1 pimap
const int PIN_SERVO_1 = 3;
const int SERVO_1_RIGHT = 2;
const int SERVO_1_LEFT = 4;
// Servo 2 pinmap
const int PIN_SERVO_2 = 9;
const int SERVO_2_RIGHT = 7;
const int SERVO_2_LEFT = 8;

// Increase angle per instruction
const int delta = 10;

Servo servo_1;
Servo servo_2;
int angle_servo_1 = 90;
int angle_servo_2 = 90;

int modify_angle(int angle, int delta);

void setup()
{
    Serial.begin(9600);
    pinMode(LED, OUTPUT);

    // Initialize Servo 1 varibles
    servo_1.attach(PIN_SERVO_1);
    servo_1.write(angle_servo_1);
    pinMode(SERVO_1_RIGHT, INPUT_PULLUP);
    pinMode(SERVO_1_LEFT, INPUT_PULLUP);
    // Initialize Servo 2 variables
    servo_2.attach(PIN_SERVO_2);
    servo_2.write(angle_servo_2);
    pinMode(SERVO_2_RIGHT, INPUT_PULLUP);
    pinMode(SERVO_2_LEFT, INPUT_PULLUP);
    
    digitalWrite(LED, LOW);
    // pinMode(4, OUTPUT);
    // digitalWrite(4, HIGH);
}

int read_right_1 = 0;
int read_left_1 = 0;
int read_right_2 = 0;
int read_left_2 = 0;

void loop()
{
    // As there is pullup resistor
    // 0 input will result as true value
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
    delay(500);
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