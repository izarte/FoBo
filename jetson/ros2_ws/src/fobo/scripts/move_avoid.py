#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import Jetson.GPIO as GPIO


from fobo.msg import Velocity
from fobo.msg import ServosPose
from geometry_msgs.msg import Vector3
from fobo.msg import Depth


class FoboMovement(Node):
    def __init__(self):
        super().__init__('FoboMovement')
        self.velocity = Velocity()
        self.pub = self.create_publisher(
            Velocity,
            'velocity',
            10
        )
        self.sub_depth_camera = self.create_subscription(
            Depth,
            'obstacle_avoiding',
            self.read_depth_turn,
            10
        )
        self.sub_depth_camera
        # self.desired_distance = 60 # cm
        self.distance = 0
        self.DISTANCE_LIMIT = 2500
        self.depth_turn = 0

    def read_depth_turn(self, msg):
        self.distance = msg.distance
        self.depth_turn = msg.obstacles
        self.velocity.linear = self.calculate_speed()
        self.velocity.angular = self.calculate_angular()
        self.pub.publish(self.velocity)

    def calculate_speed(self):
        speed = self.distance * 100 / self.DISTANCE_LIMIT
        if speed > 100:
            speed = 100
        # print(speed)
        return int(speed)

    def calculate_angular(self):
        w = -int(self.depth_turn * 50)
        if w > 100:
            return 100
        if w < -100:
            return -100
        return w

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
