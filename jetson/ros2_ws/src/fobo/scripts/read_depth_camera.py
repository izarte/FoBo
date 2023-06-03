#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from primesense import _openni2 as c_api
from primesense import openni2
import numpy as np
import heapq

from std_msgs.msg import Float32

HEIGHT = 480
WIDTH = 640

class DetectDepthCamera(Node):
    def __init__(self):
        super().__init__('ReadDepthCamera')
        self.pub = self.create_publisher(
            Float32,
            'obstacle_avoiding',
            10
        )
        timer_period = 0.1
        self.timer = self.create_timer(
            timer_period,
            self.timer_callback
        )
        self.dev = openni2.Device
        try:
            openni2.initialize()
            self.dev = openni2.Device.open_any()
            print(self.dev.get_sensor_info(openni2.SENSOR_DEPTH))
        except (RuntimeError, TypeError, NameError):
            print("puta")
            print(RuntimeError, TypeError, NameError)
        self.depth_stream = self.dev.create_depth_stream()
        self.depth_stream.set_video_mode(
            c_api.OniVideoMode(pixelFormat=c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_1_MM,
            resolutionX=WIDTH,
            resolutionY=HEIGHT,
            fps=30))
        self.depth_stream.start()

    def __del__(self):
        self.depth_stream.stop()
        openni2.unload()

    def timer_callback(self):
        msg = Float32()
        msg.data = self.read_depth_camera()
        self.pub.publish(msg)

    def read_depth_camera(self):
        frame_depth = self.depth_stream.read_frame()
        frame_depth_data = frame_depth.get_buffer_as_uint16()
        depth_array = np.ndarray((frame_depth.height, frame_depth.width), dtype=np.uint16, buffer=frame_depth_data)
        depth_array = depth_array[HEIGHT // 3:2 * HEIGHT // 3]
        
        depth_array_1d = self.create_array(depth_array)
        direction = self.calculate_direction(depth_array_1d)
        return direction

    def create_array(self, image):
        height, width = image.shape
        array = []
        image = image.T
        for j in range(width):
            m = heapq.nsmallest(25, image[j])
            array.append(max(m))
        return array

    def calculate_direction(self, array):
        left = array[:320]
        left.reverse()
        right = array[320:]
        l = len(left)
        v = 0
        for i in range(l):
            v += ((1000 - right[i]) - (1000 - left[i])) / 1000
        v /= 2 * l
        return v


def main():
    rclpy.init()
    node = DetectDepthCamera()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
