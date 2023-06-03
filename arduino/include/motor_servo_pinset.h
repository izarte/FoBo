#ifndef MOTOR_SERVO_PINSET_H

#define MOTOR_SERVO_PINSET_H

#include <Servo.h>
#include <Arduino.h>
#include <Wire.h>
#include "MPU6050.h"
#include <PID_v1.h>

// init.cpp
void init_servos();
void init_motors();
void init_gyro();

// servo.cpp
void servo_control();
void modify_angle(int *angle, int delta);
void blinkLed(int t);

// Stepper
void motors_control();
int checkLimits(int value, int min, int max);

// Gyro
void read_yaw();
void calibrateSensor();

const int LED = 13;

// PID constants
const double KP = 2;
const double KI = 5;
const double KD = 1;

// Motor 1 constant pins
const int MOTOR_1_STEP = 5;
const int MOTOR_1_DIRECTION = 11;
const int MOTOR_1_SPEED_INPUT = A0;             // Jetson 33
const int MOTOR_1_DIRECTION_INPUT = A1;         // Jetson 31 (200)

// Motor 2 constant pins
const int MOTOR_2_STEP = 6;
const int MOTOR_2_DIRECTION = 12;
const int MOTOR_2_SPEED_INPUT = A2;             // Jetson 32
const int MOTOR_2_DIRECTION_INPUT = A3;         // Jetson 35 (76)

// Servo 1 pimap
const int PIN_SERVO_1 = 3;
const int SERVO_1_INCR = 2;                    // Jetson 11 (50)
const int SERVO_1_DIR = 4;                     // Jetson 12 (79)
// Servo 2 pinmap
const int PIN_SERVO_2 = 9;
const int SERVO_2_INCR = 7;                    // Jetson 15 (194)
const int SERVO_2_DIR = 8;                     // Jetson 16 (232)

const int delta = 3;


#endif