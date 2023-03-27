#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import cv2
import numpy as np
import math

from fobo.msg import ObjectPose

class DetectCamera(Node):
    def __init__(self):
        super().__init__('ReadCamera')
        self.pub = self.create_publisher(
            ObjectPose,
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
        msg = ObjectPose()
        msg.x, msg.y, msg.distance = self.get_center_diff()
        self.pub.publish(msg)

    def get_center_diff(self):
        # Actually detect blue center and calculates its difference
        ret, frame = self.cap.read()
        if not ret:
            print("Can't see")
            return (0, 0, 0)
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

        # Find the contours in the binary mask
        contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Sort the contours in descending order of their area
        contours = sorted(contours, key=cv2.contourArea, reverse=True)

        x_dif = 0
        y_dif = 0
        distance = 0
        if len(contours) > 0:
            # Get the minimum bounding rectangle for the largest contour
            x, y, w, h = cv2.boundingRect(contours[0])

            # Draw the bounding box on the original image
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            x += int(w / 2)
            y += int(h / 2)
            # put text and highlight the center
            cv2.circle(frame, (x, y), 5, (255, 255, 255), -1)
            cv2.circle(frame, (int(frame.shape[1] / 2), int(frame.shape[0] / 2)), 5, (255, 255, 0), -1)
            # cv2.putText(frame, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            x_dif = x - frame.shape[1] / 2
            y_dif = y - frame.shape[0] / 2
            # 40 cm is w: 330 h: 192, area: 63360 hypotenuse: 381.79
            # distance1 = - (0.000130423) * (w * h) + 48.26
            distance = 381.79 * 40 / math.sqrt(w**2 + h**2)
        return (int(x_dif), int(y_dif), distance)

def main():
    rclpy.init()
    node = DetectCamera()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        rclpy.shutdown()

if __name__ == '__main__':
    main()

