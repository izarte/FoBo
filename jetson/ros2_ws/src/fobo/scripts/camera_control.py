#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import Jetson.GPIO as GPIO
import time

from fobo.msg import CameraData
from fobo.msg import ServosPose


class Servo():
    def __init__(self, incr, direction, delta=3, initial_angle=90, minimum=0, maximum=180):
        self.delta = delta
        self.incr = incr
        self.direction = direction
        GPIO.setup(self.incr, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.direction, GPIO.OUT, initial=GPIO.HIGH)
        self.initial_angle = initial_angle
        self.angle = self.initial_angle
        self.min = minimum
        self.max = maximum

    def reset_position(self):
        self.set_angle(angle=self.initial_angle)

    def set_angle(self, angle=0, incr=0):
        if incr != 0:
            angle = self.angle + incr * self.delta
        if angle > self.max:
            angle = self.max
        elif angle < self.min:
            angle = self.min
        while(self.angle != angle):
            if angle > self.angle:
                GPIO.output(self.direction, 1)
                time.sleep(1 / 1000)
                GPIO.output(self.incr, 0)
                time.sleep(10 / 1000)
                GPIO.output(self.incr, 1)
                time.sleep(10 / 1000)
                self.angle += self.delta
            else:
                GPIO.output(self.direction, 0)
                time.sleep(1 / 1000)
                GPIO.output(self.incr, 0)
                time.sleep(10 / 1000)
                GPIO.output(self.incr, 1)
                time.sleep(10 / 1000)
                self.angle -= self.delta
    
    def get_angle(self):
        return (self.angle)

class CameraControl(Node):
    def __init__(self):
        super().__init__('CameraControl')
        GPIO.setmode(GPIO.BOARD)
        self.x_motor = Servo(11, 12)
        self.y_motor = Servo(15, 16, delta=2, initial_angle=70, minimum=40, maximum=120)
        self.servos_pose = ServosPose()
        self.pub = self.create_publisher(
            ServosPose,
            'servos_pose',
            10
        )
        # timer_period = 0.1
        # self.timer = self.create_timer(
        #     timer_period,
        #     self.read_camera_pose
        # )
        self.sub = self.create_subscription(
            CameraData,
            'camera_control',
            self.read_camera_pose,
            1
        )
        self.sub
        self.range_pose_x = 120
        self.range_pose_y = 20
        self.objective_pose_y = 60
        self.time = time.time()
        self.last_view = 'left'

    def read_camera_pose(self, msg):
        # Check if person is not detected
        if msg.visible == 0.0:
            self.find_objective()
        else:
            self.move_servos(msg)
        # Publish actual servos pose
        self.servos_pose.servo_x = self.x_motor.get_angle()
        self.servos_pose.servo_y = self.y_motor.get_angle()
        self.pub.publish(self.servos_pose)

    def find_objective(self):
        self.y_motor.reset_position()
        if self.last_view == 'left':
            # print('left')
            self.x_motor.set_angle(incr=1)
            if self.x_motor.get_angle() == 180:
                self.last_view = 'right'
            # time.sleep(10 / 1000)
        elif self.last_view == 'right':
            # print('right')
            self.x_motor.set_angle(incr=-1)
            if self.x_motor.get_angle() == 0:
                self.last_view = 'left'
            # time.sleep(10 / 1000)
    
    def move_servos(self, msg):
        # Check pose to trun camera in x axis
        if msg.x > self.range_pose_x:
            # Turn right
            print("go right - ", msg.x)
            self.x_motor.set_angle(incr=-1)
            self.last_view = 'right'
        elif msg.x < -self.range_pose_x:
            # Turn left
            print("go left - ", msg.x)
            self.x_motor.set_angle(incr=1)
            self.last_view = 'left'
        # Check pose to trun camera in y axis
        if self.objective_pose_y - msg.y > self.range_pose_y:
            self.y_motor.set_angle(incr=-1)
        elif msg.y - self.objective_pose_y > self.range_pose_y:
            self.y_motor.set_angle(incr=1)


def main():
    rclpy.init()
    node = CameraControl()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        rclpy.shutdown()
        GPIO.cleanup()

if __name__ == '__main__':
    main()
