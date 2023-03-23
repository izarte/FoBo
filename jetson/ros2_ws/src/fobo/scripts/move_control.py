#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import Jetson.GPIO as GPIO

from fobo.msg import Velocity


class Motor():
	def __init__(self, pin, dir):
		GPIO.setup(pin, GPIO.OUT)
		self.pwm = GPIO.PWM(pin, 490)
		self.dc = 0
		GPIO.setup(dir, GPIO.OUT, initial=GPIO.HIGH)

	def set_speed(self, dc):
		self.dc = dc
		self.pwm.ChangeDutyCycle(self.dc)


class FoboMovement(Node):
	def __init__(self):
		super().__init__('FoboMovement')
		GPIO.setmode(GPIO.BOARD)
		self.left_motor = Motor(33, 31)
		self.right_motor = Motor(32, 35)
		self.velocity = {'linear': 0, 'angular': 0}
		self.sub = self.create_subscription(
			Velocity,
			'velocity',
			self.read_velocity,
			10
		)
		self.sub
		self.L = 0.2
		self.r = 0.1

	def read_velocity(self, msg):
		self.velocity['linear'] = msg.linear
		self.velocity['angular'] = msg.angular
	
	def move(self):
		left_wheel_speed = self.velocity['linear'] - ((self.L/2) * self.velocity['angular']) / self.r
		left_wheel_speed = self.velocity['linear'] + ((self.L/2) * self.velocity['angular']) / self.r
		self.left_motor.set_speed(left_wheel_speed)
		self.right_motor.set_speed(right_wheel_speed)

def main():
	rclpy.init()
	node = FoboMovement()
	rate = node.create_rate(2)
	try:
		while rclpy.ok():
			node.move()
			rate.sleep
	except KeyboardInterrupt:
		pass
	rclpy.shutdown()

if __name__ == '__main__':
	main()
