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
        self.sub_servo = self.create_subscription(
            ServosPose,
            "servos_pose",
            self.read_servos_pose,
            10
        )
        self.sub_depth_camera = self.create_subscription(
            Depth,
            'obstacle_avoiding',
            self.read_depth_turn,
            10
        )

        self.sub_servo
        self.desired_servo_1 = 90
        self.desired_servo_2 = 70
        # self.desired_distance = 60 # cm
        self.distance = 0
        self.DISTANCE_LIMIT = 5000
        self.depth_turn = 0

    def read_depth_turn(self, msg):
        self.distance = msg.distance
        self.depth_turn = msg.obstacles

    def read_servos_pose(self, msg):
        # print("puta")
        # self.velocity.linear = self.calculate_speed()
        if msg.servo_x > self.desired_servo_1:
            self.velocity.angular = int((msg.servo_x - self.desired_servo_1) * 100 / 90) # vel = pose * 100 % / 90º			pose goes from 0 to 90
        elif msg.servo_x < self.desired_servo_1:
            self.velocity.angular = int((msg.servo_x - self.desired_servo_1) * 100 / 90) # vel = -pose * 100 % / 90º			pose goes from 0 to -90

        # self.velocity.angular = (1.5 * (self.velocity.angluar) + 100 * self.depth_turn) / 2.5

        if msg.servo_y <= self.desired_servo_2:
            self.velocity.linear = 0
        elif msg.servo_y > self.desired_servo_2:
            # self.velocity.linear = int(self.calculate_speed())
            self.velocity.linear = 20
        # self.velocity.angular = 0
        if self.velocity.linear == 0:
            self.velocity.angular = 0
        self.pub.publish(self.velocity)

    def calculate_speed(self):
        if self.distance > self.DISTANCE_LIMIT:
            self.distance = self.DISTANCE_LIMIT
        speed = self.distance * 100 / self.DISTANCE_LIMIT
        print(speed)
        return speed

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
