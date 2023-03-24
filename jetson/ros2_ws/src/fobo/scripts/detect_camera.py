#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import cv2
import numpy as np

from fobo.msg import CameraPose

class DetectCamera(Node):
	def __init__(self):
		super().__init__('ReadCamera')
		self.pub = self.create_publisher(
			CameraPose,
			'camera_control',
			10
		)
		timer_period = 0.5
		self.timer = self.create_timer(
			timer_period,
			self.timer_callback
		)
		self.cap = cv2.VideoCapture(0)
		if not self.cap.isOpened():
			print("Can't open camera")
			exit()

	def __del__(self):
		self.cap.release()

	def timer_callback(self):
		msg = CameraPose()
		msg.x, msg.y = self.get_center_diff()
		self.pub.publish(msg)

	def get_center_diff(self):
		# Actually detect blue center and calculates its difference
		ret, frame = self.cap.read()
		if not ret:
			print("Can't read camera")
			return (0, 0)
		# Go to hsv color space
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		# Create blue range
		lower_blue = np.array([100,150,0])
		upper_blue = np.array([140,255,255])

		# Get binary mask with blue detected
		mask = cv2.inRange(hsv, lower_blue, upper_blue)
		# Close, dilate-erode and open erode-dilate to clean image
		kernel_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
		kernel_open = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
		closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_close)
		openning = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel_open)

		img = openning

		# calculate moments of binary image
		M = cv2.moments(img)
		
		# calculate x,y coordinate of center
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])
		
		x_dif = cX - frame.shape[1] / 2
		y_dif = cY - frame.shape[0] / 2
		return (int(x_dif), int(y_dif))

def main():
	rclpy.init()
	node = DetectCamera()
	try:
		rclpy.spin(node)
	except KeyboardInterrupt:
		rclpy.shutdown()

if __name__ == '__main__':
	main()

