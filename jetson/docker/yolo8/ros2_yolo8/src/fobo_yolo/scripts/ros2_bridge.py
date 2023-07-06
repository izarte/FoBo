#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import time
from geometry_msgs.msg import Vector3
import asyncio
import websockets
import json


class DetectCamera(Node):
    def __init__(self):
        super().__init__('ReadCamera')
        self.msg = Vector3()
        self.pub = self.create_publisher(
            Vector3,
            'camera_control',
            10
        )
        # self.start_server()
        start_server = websockets.serve(self.handler, "localhost", 8000)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    # async def start_server(self):
    #     server = await websockets.serve(self.handler, "localhost", 8000)
    #     await server.wait_close()
     
    async def handler(self, websocket, path):
        data = await websocket.recv()
        # print(data)
        data = json.loads(data)
        # print(data['x'])
        self.msg.x = float(data['x'])
        self.msg.y = float(data['y'])
        self.msg.z = 0.0 if data['x'] == -1 and data['y'] == -1 else 1.0 
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
 
# asyncio.get_event_loop().run_until_complete(start_server)
 
# asyncio.get_event_loop().run_forever()