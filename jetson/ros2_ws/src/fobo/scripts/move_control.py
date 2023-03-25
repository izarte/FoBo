#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import Jetson.GPIO as GPIO

from fobo.msg import Velocity
from fobo.msg import ServosPose


class FoboMovement(Node):
	def __init__(self):
		super().__init__('FoboMovement')
		self.velocity = Velocity()
		self.pub = self.create_publisher(
			Velocity,
			'velocity',
			10
		)
		self.sub = self.create_subscription(
			ServosPose,
			"servos_pose",
			self.read_servos_pose,
			10
		)
		self.sub

	def read_servos_pose(self, msg):
		self.velocity.linear = 50
		if msg.servo_x > 90:
			self.velocity.angular = int((msg.servo_x - 90) * 0.9) # vel = pose * 100 % / 90º			pose goes from 0 to 90
		elif msg.servo_x < 90:
			self.velocity.angular = int((msg.servo_x - 90) * 0.9) # vel = -pose * 100 % / 90º			pose goes from 0 to -90
		self.pub.publish(self.velocity)

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
