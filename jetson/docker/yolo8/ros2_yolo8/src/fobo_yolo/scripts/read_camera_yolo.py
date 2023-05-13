#!/usr/bin/env python3.8
import sys
import cv2
import time
import numpy as np
from websocket import create_connection
import json
from ultralytics import YOLO
import time

class DetectPerson():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Can't open camera")
            exit()
        self.model = YOLO("yolov8n.pt")
        # self.ws = create_connection("ws://localhost:8000/")
        self.data = {'x': 0, 'y': 0}
        self.detect_person()

    def __del__(self):
        self.cap.release()

    def detect_person(self):
        # Actually detect blue center and calculates its difference
        t = time.time()
        ws = create_connection("ws://localhost:8000/")
        ret, frame = self.cap.read()
        if not ret:
            print("Can't see")

        result = model.track(frame, agnostic_nms=True, show=False, device=0, classes=0, tracker="botsort.yaml")[0]
        boxes = result.boxes.cpu()
        if boxes:
            x = int(boxes.xyxy[0][0] + ((boxes.xyxy[0][2] - boxes.xyxy[0][0]).item() / 2))
            y = int(boxes.xyxy[0][1] + ((boxes.xyxy[0][3] - boxes.xyxy[0][1]).item() / 2))
            print(x, y)
            self.data['x'] = x - frame.shape[1] / 2
            self.data['y'] = y - frame.shape[0] / 2
        else:
            self.data = {'x': 0, 'y': 0}
        print(self.data['x'], self.data['y'])

        # self.ws.send(json.dumps(self.data))
        ws.send(json.dumps(self.data))
        ws.close()
        print("Time: ", time.time() - t)
        self.detect_person()

def main():
    try:
        detect = DetectPerson()
        # detect.detect_person()
    except KeyboardInterrupt:
        # detect.ws.close()
        sys.exit()

if __name__ == '__main__':
    main()
