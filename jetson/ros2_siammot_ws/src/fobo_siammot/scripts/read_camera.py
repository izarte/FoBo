#!/usr/bin/env python3
import sys
import cv2
import rclpy
from rclpy.node import Node
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge
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
        timer_period = 0.05
        self.timer = self.create_timer(
            timer_period,
            self.timer_callback
        )
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


        self.vis_generator = VisGenerator(vis_height=1080)
        # self.vis_writer = VisWriter(
        #                     dump_video=False,
        #                     out_path=None,
        #                     file_name=None)
        self.tracker = DemoInference(
                        track_class='person',
                        vis_generator=self.vis_generator
                    )
        self.detect_person()



    def __del__(self):
        self.cap.release()

    def timer_callback(self):
        self.detect_person()

    def detect_person(self):
        # Actually detect blue center and calculates its difference
        ret, frame = self.cap.read()
        if not ret:
            print("Can't see")

            # convert image to message
        # video_reader = build_video_iterator(frame)
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # results = list(self.tracker.process_frame_sequence(frame))
        results, center = self.tracker.process_frame_sequence(frame)
        x_dif = int((center[0] - frame.shape[1]) / 2)
        y_dif = int((center[1] - frame.shape[0]) / 2)
        print(x_dif, y_dif)
        # cv2.circle(results, (center[0], center[1]), 25, (0, 0, 255), -1)
        # cv2.circle(results, (int(results.shape[1] / 2), int(results.shape[0] / 2)), 25, (255, 255, 0), -1)
        # msg = self.bridge.cv2_to_imgmsg(results, encoding='bgr8')
        self.msg.x = float(x_dif)
        self.msg.y = float(y_dif)

        # publish message
        self.pub.publish(self.msg)

def main():
    rclpy.init()
    node = DetectCamera()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
