#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import Jetson.GPIO as GPIO
import simple_pid

from fobo.msg import Velocity
from std_msgs.msg import Float32

Kp = 6
Ki = 2
Kd = 3


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


class MotorsControl(Node):
    def __init__(self):
        super().__init__('MotorsControl')
        GPIO.setmode(GPIO.BOARD)
        self.left_motor = Motor(33, 31, invert=True)
        self.right_motor = Motor(32, 35)
        # self.left_motor = Motor(32, 35)
        # self.right_motor = Motor(33, 31)

        self.velocity = Velocity()
        self.sub = self.create_subscription(
            Velocity,
            'velocity',
            self.read_velocity,
            10
        )
        self.sub_imu = self.create_subscription(
            Float32,
            'yaw_orientation',
            self.read_imu,
            10
        )
        self.sub
        self.sub_imu
        self.L = 0.2
        self.r = 0.1
        self.pid = simple_pid.PID(Kp, Ki, Kd)
        self.pid.output_limits = (-50, 50)
        self.yaw = 0
        self.last_linear = 0
        self.last_angular = 0
    
    def __del__(self):
        self.left_motor.set_speed(0)
        self.right_motor.set_speed(0)
        del(self.left_motor)
        del(self.right_motor)

    def read_imu(self, msg):
        self.yaw = msg.data

    def read_velocity(self, msg):
        self.velocity.linear = msg.linear
        self.velocity.angular = msg.angular
        left_wheel_speed = self.velocity.linear + ((self.L/2) * self.velocity.angular) / self.r
        right_wheel_speed = self.velocity.linear - ((self.L/2) * self.velocity.angular) / self.r
        # right_wheel_speed = -right_wheel_speed
        left_wheel_speed, right_wheel_speed = self.check_limits(left_wheel_speed, right_wheel_speed)
        self.left_motor.set_speed(left_wheel_speed)
        self.right_motor.set_speed(right_wheel_speed)
        print(f"left: {left_wheel_speed} right: {right_wheel_speed}")

    def check_limits(self, right, left):
        if left > 100:
            left = 100
        elif left < 0:
            left = 0
        if right > 100:
            right = 100
        elif right < 0:
            right = 0
        return (left, right)

    def process_pid(self, linear, angular):
        if angluar == 0:
            if self.last_linear != linear:
                self.pid.setpoint = self.yaw
            return (self.pid(self.yaw))
        return (0)


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
