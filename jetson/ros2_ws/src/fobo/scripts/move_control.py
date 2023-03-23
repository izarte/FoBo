#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import Jetson.GPIO as GPIO

from fobo.msg import Velocity


class Motor():
	def __init__(self, pin, direction):
		GPIO.setup(pin, GPIO.OUT)
		self.pwm = GPIO.PWM(pin, 490)
		self.dir = direction
		self.dc = 0
		GPIO.setup(self.dir, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.output(self.dir, GPIO.HIGH)
		self.pwm.start(self.dc)

	def __del__(self):
		self.pwm.stop()

	def set_speed(self, dc):
		self.dc = dc
		if self.dc < 0:
			GPIO.output(self.dir, GPIO.LOW)
			self.dc = -self.dc
		else:
			GPIO.output(self.dir, GPIO.HIGH)
		if self.dc > 100:
			self.dc = 100
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
		left_wheel_speed = self.velocity['linear'] - ((self.L/2) * self.velocity['angular']) / self.r
		right_wheel_speed = self.velocity['linear'] + ((self.L/2) * self.velocity['angular']) / self.r
		self.left_motor.set_speed(left_wheel_speed)
		self.right_motor.set_speed(right_wheel_speed)
		print(f"left: {left_wheel_speed} right: {right_wheel_speed}")


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
