#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import Jetson.GPIO as GPIO
import time

from fobo.msg import CameraPose
from fobo.msg import ServosPose


class Servo():
	def __init__(self, incr, direction):
		self.delta = 10
		self.incr = incr
		self.direction = direction
		GPIO.setup(self.incr, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(self.direction, GPIO.OUT, initial=GPIO.HIGH)
		self.angle = 90
	
	def incr_angle(self, direction):
		angle = self.angle + direction * self.delta
		if angle > 180:
			angle = 180
		elif angle < 0:
			angle = 0
		self.set_angle(angle)
		
	def set_angle(self, angle):
		while(self.angle != angle):
			if angle > self.angle:
				GPIO.output(self.direction, 1)
				GPIO.output(self.incr, 0)
				time.sleep(10 / 1000)
				GPIO.output(self.incr, 1)
				time.sleep(10 / 1000)
				self.angle += self.delta
			else:
				GPIO.output(self.direction, 0)
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
		self.y_motor = Servo(15, 16)
		self.servos_pose = ServosPose()
		self.pub = self.create_publisher(
			ServosPose,
			'servos_pose',
			10
		)
		self.sub = self.create_subscription(
			CameraPose,
			'camera_control',
			self.read_camera_pose,
			10
		)
		self.sub
		self.range_pose_x = 10
		self.range_pose_y = 10

	def read_camera_pose(self, msg):
		if msg.x > self.range_pose_x:
			self.x_motor.incr_angle(1)
		elif msg.x < -self.range_pose_x:
			self.x_motor.incr_angle(-1)
		
		if msg.y > self.range_pose_y:
			self.y_motor.incr_angle(1)
		elif msg.y < -self.range_pose_y:
			self.y_motor.incr_angle(-1)

		self.servos_pose.servo_x = self.x_motor.get_angle()
		self.servos_pose.servo_y = self.y_motor.get_angle()
		self.pub.publish(self.servos_pose)
		# self.x_motor.set_angle(msg.x)
		# self.y_motor.set_angle(msg.y)

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
