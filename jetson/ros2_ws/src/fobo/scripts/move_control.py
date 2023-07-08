#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import Jetson.GPIO as GPIO


from fobo.msg import Velocity
from fobo.msg import ServosPose
from geometry_msgs.msg import Vector3
from fobo.msg import Depth

'''
Ros2 node to calculate linear and angular speed based on servos angle and forward obstacles
Subs:
    servos_pose
    obstacile_avoiding
Pubs:
    velocity

All commented code is due to Jetson capacity limitations so can't realisitic work with 2 cameras at same time
'''
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
        # self.sub_depth_camera = self.create_subscription(
        #     Depth,
        #     'obstacle_avoiding',
        #     self.read_depth_turn,
        #     10
        # )

        self.sub_servo
        self.desired_servo_1 = 90
        self.desired_servo_2 = 70
        self.x_offset = 10
        # self.desired_distance = 60 # cm
        # self.distance = 0
        # self.DISTANCE_LIMIT = 5000
        # self.depth_turn = 0

    # def read_depth_turn(self, msg):
    #     self.distance = msg.distance
    #     self.depth_turn = msg.obstacles

    def read_servos_pose(self, msg):
        # self.velocity.linear = self.calculate_speed()
        dif = self.desired_servo_1 - msg.servo_x
        self.velocity.angular = int((dif if abs(dif) > self.x_offset else 0) * 100 / 90)

        # obstacle_angular = self.calculate_angular()

        # self.velocity.angluar = check_limits(self.velocity.angluar + obstacle_angular, 100, -100)

        # self.velocity.angular = (1.5 * (self.velocity.angluar) + 100 * self.depth_turn) / 2.5

        if msg.servo_y <= self.desired_servo_2:
            self.velocity.linear = 0
        elif msg.servo_y > self.desired_servo_2:
            # self.velocity.linear = int(self.calculate_speed())
            self.velocity.linear = 15
        # self.velocity.angular = 0
        if self.velocity.linear == 0:
            self.velocity.angular = 0
        self.pub.publish(self.velocity)

    # def calculate_speed(self):
    #     if self.distance > self.DISTANCE_LIMIT:
    #         self.distance = self.DISTANCE_LIMIT
    #     speed = self.distance * 100 / self.DISTANCE_LIMIT
    #     print(speed)
    #     return speed

    # def calculate_angular(self):
    #     w = -int(self.depth_turn * 50)
    #     w = self.check_limits(n, 100, -100)
    #     return w

    # def check_limits(n, maxim, minim):
    #     if n > maxim:
    #         return maxim
    #     if n < minim:
    #         return minim
    #     return n

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
