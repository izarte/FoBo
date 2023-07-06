from ultralytics import YOLO
import numpy
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

model_name = 'yolov8n' #@param ["yolov8n", "yolov8s", "yolov8m", "yolov8l", "yolov8x"]
# input_width = 640 #@param {type:"slider", min:32, max:4096, step:32}
input_width = 1533 #@param {type:"slider", min:32, max:4096, step:32}
input_height = 480 #@param {type:"slider", min:32, max:4096, step:32}
input_height = 2048 #@param {type:"slider", min:32, max:4096, step:32}
optimize_cpu = False

model = YOLO(f"{model_name}.pt") 
opset_version = 11
# results = model.predict(source=frame)[0]
model.export(format="onnx", opset=opset_version, imgsz=[input_width, input_height], device=0, half=False, task='detect')