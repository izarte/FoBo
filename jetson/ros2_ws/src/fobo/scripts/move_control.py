#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import Jetson.GPIO as GPIO

from fobo.msg import Velocity
from fobo.msg import ServosPose
from fobo.msg import ObjectPose


class FoboMovement(Node):
    def __init__(self):
        super().__init__('FoboMovement')
        self.velocity = Velocity()
        self.pub = self.create_publisher(
            Velocity,
            'velocity',
            10
        )
        self.sub_servo = self.create_subscription(
            ServosPose,
            "servos_pose",
            self.read_servos_pose,
            10
        )
        self.sub_camera = self.create_subscription(
            ObjectPose,
            'camera_control',
            self.read_distance,
            10
        )
        self.sub_servo
        self.sub_camera
        self.desired_distance = 60 # cm
        self.distance = 0

    def read_distance(self, msg):
        self.distance = msg.distance

    def read_servos_pose(self, msg):

        self.velocity.linear = self.calculate_speed()
        if msg.servo_x > 90:
            self.velocity.angular = int((msg.servo_x - 90) * 0.9) # vel = pose * 100 % / 90º			pose goes from 0 to 90
        elif msg.servo_x < 90:
            self.velocity.angular = int((msg.servo_x - 90) * 0.9) # vel = -pose * 100 % / 90º			pose goes from 0 to -90
        # self.velocity.angular = 0
        if self.velocity.linear == 0:
            self.velocity.angular = 0
        self.pub.publish(self.velocity)

    def calculate_speed(self):
        # Calculate speed based on distance to stay at desired_distance
        if self.distance < self.desired_distance:
            return 0
        # max speed will be at double desired speed
        return (int(100 * self.distance / (2 * self.desired_distance)) - 50)

def main():
    rclpy.init()
    node = FoboMovement()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        rclpy.shutdown()
        GPIO.cleanup()

if __name__ == '__main__':
    main()
