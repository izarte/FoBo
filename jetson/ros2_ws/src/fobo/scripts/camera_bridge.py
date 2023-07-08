#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import time
from fobo.msg import CameraData
import asyncio
import websockets
import json


"""
Ros2 node to create websocket server to recieve tracking module exit
Subs:

Pubs:
    camera_control
"""
class DetectCamera(Node):
    def __init__(self):
        super().__init__('ReadCamera')
        self.msg = CameraData()
        self.pub = self.create_publisher(
            CameraData,
            'camera_control',
            10
        )
        start_server = websockets.serve(self.handler, "0.0.0.0", 8000)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    async def handler(self, websocket, path):
        data = await websocket.recv()
        # print(data)
        data = json.loads(data)
        # print(data['x'])
        self.msg.x = int(data['x'])
        self.msg.y = int(data['y'])
        self.msg.visible = 0 if data['x'] == -1 and data['y'] == -1 else 1 
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
