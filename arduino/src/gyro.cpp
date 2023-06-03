#include "motor_servo_pinset.h"

extern MPU6050 mpu;

// Calibration constants
extern float gyroZOffset;

// void setup() {
//   // Initialize serial communication
//   Serial.begin(9600);

//   // Initialize the MPU-6050
//   Wire.begin();
//   mpu.initialize();

//   // Calibrate the sensor
//   calibrateSensor();
// }
extern float yaw;

void read_yaw()
{
    int16_t gyroX, gyroY, gyroZ;
    mpu.getRotation(&gyroX, &gyroY, &gyroZ);
    float gyroZf = (gyroZ - gyroZOffset) / 131.0;
    yaw = yaw + (gyroZf * 0.01);
    Serial.print("Yaw: ");
    Serial.print(yaw);
    // return (yaw);
}

// void loop() {
//   // Read raw gyro values
//   int16_t gyroX, gyroY, gyroZ;
//   mpu.getRotation(&gyroX, &gyroY, &gyroZ);

//   // Apply calibration offsets
//   float gyroXf = (gyroX - gyroXOffset) / 131.0;
//   float gyroYf = (gyroY - gyroYOffset) / 131.0;
//   float gyroZf = (gyroZ - gyroZOffset) / 131.0;

//   // Calculate roll, pitch, and yaw angles
//   roll = roll + (gyroXf * 0.01);
//   pitch = pitch + (gyroYf * 0.01);
//   yaw = yaw + (gyroZf * 0.01);

//   // Print the roll, pitch, and yaw values
//   Serial.print("Roll: ");
//   Serial.print(roll);
//   Serial.print("\tPitch: ");
//   Serial.print(pitch);
//   Serial.print("\tYaw: ");
//   Serial.println(yaw);

//   delay(10);
// }

void calibrateSensor() 
{
    // Read the gyro values multiple times to calculate the offsets
    int numReadings = 100;
    for (int i = 0; i < numReadings; i++) {
      int16_t gyroX, gyroY, gyroZ;
      mpu.getRotation(&gyroX, &gyroY, &gyroZ);
      gyroZOffset += gyroZ;
      delay(10);
    }

    // Calculate the average offsets
    gyroZOffset /= numReadings;
}
