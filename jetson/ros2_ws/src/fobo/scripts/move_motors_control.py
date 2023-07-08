#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import Jetson.GPIO as GPIO
import simple_pid
import smbus
import time

from fobo.msg import Velocity
from std_msgs.msg import Float32


#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
# Truly is X axis in gyroscope
GYRO_ZOUT_H  = 0x43
# GYRO_ZOUT_H  = 0x47
Device_Address = 0x68 


"""
Class to calibrate, check well working, read imu and calculate yaw
"""
class IMU():
    def __init__(self):
        self.offset = 0
        self.yaw = 0.0
        self.last_yaw = 0.0
        self.bus = smbus.SMBus(1)
        self.MPU_Init()
        self.calibrate()
        self.prev_time = time.monotonic()


    def MPU_Init(self):
        #write to sample rate register
        self.bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
        
        #Write to power management register
        self.bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
        
        #Write to Configuration register
        self.bus.write_byte_data(Device_Address, CONFIG, 0)
        
        #Write to Gyro configuration register
        self.bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
        
        #Write to interrupt enable register
        self.bus.write_byte_data(Device_Address, INT_ENABLE, 1)

    def read_raw_data(self, addr):
        #Accelero and Gyro value are 16-bit
        high = self.bus.read_byte_data(Device_Address, addr)
        low = self.bus.read_byte_data(Device_Address, addr+1)
     
        #concatenate higher and lower value
        value = ((high << 8) | low)
         
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return -value

    def calibrate(self):
        num_samples = 100
        self.offset = 0
        for _ in range(num_samples):
            self.offset += self.read_raw_data(GYRO_ZOUT_H)
            time.sleep(0.01)  # Delay between samples

        prev_time = time.monotonic()
        self.offset = self.offset / num_samples
    
    def update_yaw(self):
        current_time = time.monotonic()

        gyro_z = self.read_raw_data(GYRO_ZOUT_H)
        Gz = (gyro_z - self.offset) / 131.0
        self.yaw = self.yaw + (Gz * (current_time - self.prev_time))
        self.prev_time = current_time
        if abs(self.last_yaw - self.yaw) < 0.001:
            self.yaw = self.last_yaw
        self.last_yaw = self.yaw
    
    def get_yaw(self):
        return self.yaw

    def test_IMU(self):
        num_samples = 100
        for _ in range(num_samples):
            self.update_yaw()
            time.sleep(0.01)
        if abs(self.yaw) > 0.01:
            return 1
        return 0


"""
Class to control speed and direction of single motor (based on pin communication with Arduino)
"""
class Motor():
    def __init__(self, pin, direction, invert=False):
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, 490)
        self.dir = direction
        self.dc = 0
        self.i = invert
        GPIO.setup(self.dir, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.output(self.dir, GPIO.LOW)
        self.pwm.start(self.dc)

    def __del__(self):
        self.pwm.stop()

    def set_speed(self, dc):
        self.dc = dc
        if self.dc < 0:
            GPIO.output(self.dir, GPIO.HIGH)
            if self.i:
                GPIO.output(self.dir, GPIO.LOW)
            self.dc = -self.dc
        else:
            GPIO.output(self.dir, GPIO.LOW)
            if self.i:
                GPIO.output(self.dir, GPIO.HIGH)
        if self.dc > 100:
            self.dc = 100
        self.pwm.ChangeDutyCycle(self.dc)


"""
Class to compute pid controller
"""
class pidObject():
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.pid = simple_pid.PID(self.Kp, self.Ki, self.Kd, setpoint = 0)
        self.pid.output_limits = (-30, 30)
   
    def reset(self):
        self.pid.reset()

    def update_target(self, target):
        self.pid.setpoint = target
    
    def execute_pid(self, yaw):
        return self.pid(yaw)


"""
Ros2 node to control each motor speed based on calculated velocity
Subs:
    velocity
    # yaw_orientation

Imu code should be in another ros2 node, it is present en read_imu.py
Due to RAM limitation, both nodes are unified because only this node 
needs imu information and is more efficient in RAM terms.
"""
class MotorsControl(Node):
    def __init__(self):
        super().__init__('MotorsControl')
        GPIO.setmode(GPIO.BOARD)
        self.left_motor = Motor(33, 35)
        self.right_motor = Motor(32, 31, invert=True)

        self.velocity = Velocity()
        self.sub = self.create_subscription(
            Velocity,
            'velocity',
            self.read_velocity,
            10
        )
        # self.sub_imu = self.create_subscription(
        #     Float32,
        #     'yaw_orientation',
        #     self.read_imu,
        #     10
        # )

        timer_period = 0.1
        self.timer = self.create_timer(
            timer_period,
            self.calculate_movement
        )

        self.sub
        # self.sub_imu
        self.L = 0.2
        self.r = 0.1
        self.yaw = 0
        self.pid = pidObject(Kp=6, Ki=2, Kd=3)
        self.velocity.linear = 0
        self.velocity.angular = 0
        self.last_linear = 0
        self.change = 1

        # No need if read_imu node is present
        self.imu = IMU()
        while self.imu.test_IMU():
            self.imu = IMU()
        print("DONE")
    
    def __del__(self):
        self.left_motor.set_speed(0)
        self.right_motor.set_speed(0)
        del(self.left_motor)
        del(self.right_motor)

    # Uncomment if read_imu node
    # def read_imu(self, msg):
    #     self.yaw = msg.data

    def read_velocity(self, msg):
        self.velocity.linear = msg.linear
        self.velocity.angular = msg.angular
        self.check_change()
        self.calculate_movement()
    
    def calculate_movement(self):
        left_wheel_speed = self.velocity.linear + ((self.L/2) * self.velocity.angular) / self.r
        right_wheel_speed = self.velocity.linear - ((self.L/2) * self.velocity.angular) / self.r

        control_signal = 0
        if self.velocity.angular == 0:
            self.yaw = self.imu.get_yaw()
            if self.change:
                self.change = 0
                self.pid.reset()
                self.pid.update_target(self.yaw)
            control_signal = self.pid.execute_pid(self.yaw)
        
        if self.velocity.linear > 0:
            left_wheel_speed, right_wheel_speed = self.control_speeds(left_wheel_speed, right_wheel_speed, control_signal, 10, 50)
        # if control_signal > 0:
        #     self.get_logger().info(f"PID - left: {left_wheel_speed} right: {right_wheel_speed} cs: {control_signal}")
        # else:
        #     self.get_logger().info(f"left: {left_wheel_speed} right: {right_wheel_speed} cs: {control_signal}")
        self.left_motor.set_speed(left_wheel_speed)
        self.right_motor.set_speed(right_wheel_speed)
    
    def check_change(self):
        return self.change or self.last_linear - self.velocity.linear

    def control_speeds(self, left, right, control_signal, minim, maxim):
        left += control_signal
        right -= control_signal

        if right > left and right > maxim:
            left = maxim - (right - left)
            right = maxim
        if left > right and left > maxim:
            right = maxim - (left - right)
            left = maxim
        
        if left < minim:
            left = minim
        if right < minim:
            right = minim
        return left, right


def main():
    rclpy.init()
    node = MotorsControl()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        rclpy.shutdown()
        GPIO.cleanup()


if __name__ == '__main__':
    main()
