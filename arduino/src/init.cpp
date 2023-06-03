#include "motor_servo_pinset.h"

// Servos variables
Servo servo_1;
Servo servo_2;
int angle_servo_1 = 90;
int angle_servo_2 = 90;

MPU6050 mpu;
float gyroZOffset = 0.0;
float yaw = 0.0;

//Define Variables we'll be connecting to
double Setpoint = 0.0, Input, Output;

//Specify the links and initial tuning parameters
double Kp=3, Ki=0, Kd=0.2;
PID movement_PID(&Input, &Output, &Setpoint, Kp, Ki, Kd, DIRECT);

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

    movement_PID.SetMode(AUTOMATIC);
}

void init_gyro()
{
    // Initialize the MPU-6050
    Wire.begin();
    mpu.initialize();
  
    // Calibrate the sensor
    calibrateSensor();
}