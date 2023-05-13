#!/usr/bin/env python3
import sys
import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import time
import numpy as np
from geometry_msgs.msg import Vector3

sys.path.insert(0, "/ros2_ws/src/fobo_siammot/recognition")

from demos.demo_inference import DemoInference
from demos.utils.vis_generator import VisGenerator
from demos.utils.vis_writer import VisWriter
from demos.video_iterator import build_video_iterator


class DetectCamera(Node):
    def __init__(self):
        super().__init__('ReadCamera')
        # timer_period = 0.05
        # self.timer = self.create_timer(
        #     timer_period,
        #     self.timer_callback
        # )
        self.cap = cv2.VideoCapture(0)
        self.msg = Vector3()
        self.pub = self.create_publisher(
            Vector3,
            'camera_control',
            10
        )
        # self.bridge = CvBridge()
        if not self.cap.isOpened():
            print("Can't open camera")
            exit()

        # self.pub_img = self.create_publisher(
        #     Image,
        #     'image_topic',
        #     10
        # )
        self.model = YOLO("yolov8n.pt")
        self.detect_person()

    def __del__(self):
        self.cap.release()

    # def timer_callback(self):
    #     self.detect_person()

    def detect_person(self):
        # Actually detect blue center and calculates its difference
        t = time.time()
        ret, frame = self.cap.read()
        if not ret:
            print("Can't see")

        # convert image to message
        # g_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        result = model.track(frame, agnostic_nms=True, device=0, classes=0)[0]
        boxes = result.boxes.cpu()
        if boxes:
            x = int(boxes.xyxy[0][0] + ((boxes.xyxy[0][2] - boxes.xyxy[0][0]).item() / 2))
            y = int(boxes.xyxy[0][1] + ((boxes.xyxy[0][3] - boxes.xyxy[0][1]).item() / 2))
            print(x, y)
            x_dif = x - frame.shape[1] / 2
            y_dif = y - frame.shape[0] / 2
        else:
            x_dif = 0
            y_dif = 0
        print(x_dif, y_dif)

        # cv2.circle(results, (center[0], center[1]), 25, (0, 0, 255), -1)
        # cv2.circle(results, (int(results.shape[1] / 2), int(results.shape[0] / 2)), 25, (255, 255, 0), -1)
        # msg = self.bridge.cv2_to_imgmsg(results, encoding='bgr8')
        # self.pub_img.publish(
        #     msg)
        self.msg.x = float(x_dif)
        self.msg.y = float(y_dif)

        # publish message
        self.pub.publish(self.msg)
        print("Time: ", time.time() - t)
        self.detect_person()

def main():
    rclpy.init()
    node = DetectCamera()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
