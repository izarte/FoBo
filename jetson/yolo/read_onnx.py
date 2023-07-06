# import cv2
# import numpy as np
# from PIL import Image

# # Load Model
# net = cv2.dnn.readNet('yolov8n.onnx')

# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)

# INPUT_WIDTH = 640
# INPUT_HEIGHT = 480
# SCORE_THRESHOLD = 0.6
# NMS_THRESHOLD = 0.6
# CONFIDENCE_THRESHOLD = 0.8

# # Define yolov8 classes
# CLASESS_YOLO = [
#  'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 
#  'traffic light', 'fire hydrant', 'street sign', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 
#  'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'hat', 'backpack', 'umbrella', 
#  'shoe', 'eye glasses', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 
#  'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'plate', 
#  'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 
#  'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'mirror', 
#  'dining table', 'window', 'desk', 'toilet', 'door', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 
#  'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'blender', 'book', 'clock', 'vase',
#  'scissors', 'teddy bear', 'hair drier', 'toothbrush'
# ]

# image = cv2.imread('NO_SUBIR.jpeg')
# blob = cv2.dnn.blobFromImage(image, 1/255.0, (INPUT_WIDTH, INPUT_HEIGHT), swapRB=True, crop=False)
# net.setInput(blob)
# preds = net.forward()
# preds = preds.transpose((0, 2, 1))


# # Extract output detection
# class_ids, confs, boxes = list(), list(), list()

# image_height, image_width, _ = image.shape
# x_factor = image_width / INPUT_WIDTH
# y_factor = image_height / INPUT_HEIGHT

# rows = preds[0].shape[0]

# for i in range(rows):
#     row = preds[0][i]
#     conf = row[4]
    
#     classes_score = row[4:]
#     _,_,_, max_idx = cv2.minMaxLoc(classes_score)
#     class_id = max_idx[1]
#     if (classes_score[class_id] > .25):
#         confs.append(conf)
#         label = CLASESS_YOLO[int(class_id)]
#         class_ids.append(label)
        
#         #extract boxes
#         x, y, w, h = row[0].item(), row[1].item(), row[2].item(), row[3].item() 
#         left = int((x - 0.5 * w) * x_factor)
#         top = int((y - 0.5 * h) * y_factor)
#         width = int(w * x_factor)
#         height = int(h * y_factor)
#         box = np.array([left, top, width, height])
#         boxes.append(box)
        
# r_class_ids, r_confs, r_boxes = list(), list(), list()

# indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.25, 0.45) 
# for i in indexes:
#     r_class_ids.append(class_ids[i])
#     r_confs.append(confs[i])
#     r_boxes.append(boxes[i])

# for i in indexes:
#     box = boxes[i]
#     left = box[0]
#     top = box[1]
#     width = box[2]
#     height = box[3]
    
#     cv2.rectangle(image, (left, top), (left + width, top + height), (0,255,0), 3)
# Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

# cv2.imshow("image", image)
# cv2.waitKey(0)



#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################



# import onnxruntime
# import cv2
# import numpy as np
# from PIL import Image


# opt_session = onnxruntime.SessionOptions()
# opt_session.enable_mem_pattern = False
# opt_session.enable_cpu_mem_arena = False
# opt_session.graph_optimization_level = onnxruntime.GraphOptimizationLevel.ORT_DISABLE_ALL

# model_path = 'yolov8n.onnx'
# EP_list = ['CUDAExecutionProvider', 'CPUExecutionProvider']

# ort_session = onnxruntime.InferenceSession(model_path, providers=EP_list)

# model_inputs = ort_session.get_inputs()
# input_names = [model_inputs[i].name for i in range(len(model_inputs))]
# input_shape = model_inputs[0].shape
# print(input_shape)

# model_output = ort_session.get_outputs()
# output_names = [model_output[i].name for i in range(len(model_output))]

# image = cv2.imread('NO_SUBIR.jpeg')
# image_height, image_width = image.shape[:2]
# Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# input_height, input_width = input_shape[2:]
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# resized = cv2.resize(image_rgb, (input_width, input_height))
# input_image = resized / 255.0
# input_image = input_image.transpose(2,0,1)
# input_tensor = input_image[np.newaxis, :, :, :].astype(np.float32)
# input_tensor.shape
# outputs = ort_session.run(output_names, {input_names[0]: input_tensor})[0]

# predictions = np.squeeze(outputs).T
# conf_thresold = 0.8
# # Filter out object confidence scores below threshold
# scores = np.max(predictions[:, 4:], axis=1)
# predictions = predictions[scores > conf_thresold, :]
# scores = scores[scores > conf_thresold]

# # Get the class with the highest confidence
# class_ids = np.argmax(predictions[:, 4:], axis=1)

# # Get bounding boxes for each object
# boxes = predictions[:, :4]

# #rescale box
# input_shape = np.array([input_width, input_height, input_width, input_height])
# boxes = np.divide(boxes, input_shape, dtype=np.float32)
# boxes *= np.array([image_width, image_height, image_width, image_height])
# boxes = boxes.astype(np.int32)

# def nms(boxes, scores, iou_threshold):
#     # Sort by score
#     sorted_indices = np.argsort(scores)[::-1]

#     keep_boxes = []
#     while sorted_indices.size > 0:
#         # Pick the last box
#         box_id = sorted_indices[0]
#         keep_boxes.append(box_id)

#         # Compute IoU of the picked box with the rest
#         ious = compute_iou(boxes[box_id, :], boxes[sorted_indices[1:], :])

#         # Remove boxes with IoU over the threshold
#         keep_indices = np.where(ious < iou_threshold)[0]

#         # print(keep_indices.shape, sorted_indices.shape)
#         sorted_indices = sorted_indices[keep_indices + 1]

#     return keep_boxes

# def compute_iou(box, boxes):
#     # Compute xmin, ymin, xmax, ymax for both boxes
#     xmin = np.maximum(box[0], boxes[:, 0])
#     ymin = np.maximum(box[1], boxes[:, 1])
#     xmax = np.minimum(box[2], boxes[:, 2])
#     ymax = np.minimum(box[3], boxes[:, 3])

#     # Compute intersection area
#     intersection_area = np.maximum(0, xmax - xmin) * np.maximum(0, ymax - ymin)

#     # Compute union area
#     box_area = (box[2] - box[0]) * (box[3] - box[1])
#     boxes_area = (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])
#     union_area = box_area + boxes_area - intersection_area

#     # Compute IoU
#     iou = intersection_area / union_area

#     return iou

# # Apply non-maxima suppression to suppress weak, overlapping bounding boxes
# indices = nms(boxes, scores, 0.3)

# # Define classes 
# CLASSES = [
#  'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 
#  'traffic light', 'fire hydrant', 'street sign', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 
#  'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'hat', 'backpack', 'umbrella', 
#  'shoe', 'eye glasses', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 
#  'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'plate', 
#  'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 
#  'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'mirror', 
#  'dining table', 'window', 'desk', 'toilet', 'door', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 
#  'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'blender', 'book', 'clock', 'vase',
#  'scissors', 'teddy bear', 'hair drier', 'toothbrush'
# ]

# def xywh2xyxy(x):
#     # Convert bounding box (x, y, w, h) to bounding box (x1, y1, x2, y2)
#     y = np.copy(x)
#     y[..., 0] = x[..., 0] - x[..., 2] / 2
#     y[..., 1] = x[..., 1] - x[..., 3] / 2
#     y[..., 2] = x[..., 0] + x[..., 2] / 2
#     y[..., 3] = x[..., 1] + x[..., 3] / 2
#     return y

# image_draw = image.copy()
# for (bbox, score, label) in zip(xywh2xyxy(boxes[indices]), scores[indices], class_ids[indices]):
#     bbox = bbox.round().astype(np.int32).tolist()
#     cls_id = int(label)
#     cls = CLASSES[cls_id]
#     color = (0,255,0)
#     cv2.rectangle(image_draw, tuple(bbox[:2]), tuple(bbox[2:]), color, 2)
#     cv2.putText(image_draw,
#                 f'{cls}:{int(score*100)}', (bbox[0], bbox[1] - 2),
#                 cv2.FONT_HERSHEY_SIMPLEX,
#                 0.60, [225, 255, 255],
#                 thickness=1)

# cv2.imshow("image", image_draw)
# cv2.waitKey(0)



#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################



import cv2
import supervision as sv
from ultralytics import YOLO
import time
import numpy as np
# from bytetracker import BYTETracker


def main():
    # define resolution
    cap = cv2.VideoCapture(0)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # specify the model
    model = YOLO("yolov8n.onnx")
    # byte_tracker = BYTETracker()

    first = True

    # customize the bounding box
    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,
        text_scale=1
    )


    while True:
        t = time.time()
        ret, frame = cap.read()
        # frame = cv2.pyrDown(frame)
        # result = model(frame, agnostic_nms=True, device=0, classes=0)[0]
    # for result in model.track(source=0, stream=True, agnostic_nms=True, show=False, device=0, classes=0, tracker="bytetrack.yaml"):
        result = model.track(
            source=frame,
            # task='detect',
            # agnostic_nms=True,
            classes=0,
            device=0,
            format='onnx',
            tracker="botsort.yaml",
            half=True,
            verbose=False,
        )[0]
        t1 = time.time()
        # frame = result.orig_frame
        # result = model.predict(source=0, device=0, classes=0)
        boxes = result.boxes.cpu()
        # print(boxes.xyxy[0].size())
        x = 0
        y = 0
        if result.boxes.id is not None:
            # id = result.boxes.id.cpu().numpy().astype(int)
            x = int(boxes.xyxy[0][0] + ((boxes.xyxy[0][2] - boxes.xyxy[0][0]).item() / 2))
            y = int(boxes.xyxy[0][1] + ((boxes.xyxy[0][3] - boxes.xyxy[0][1]).item() / 2))
            print(x, y)
            x_dif = x - frame.shape[1] / 2
            y_dif = y - frame.shape[0] / 2
        else:
            x_dif = 0
            y_dif = 0
        t2 = time.time()
        # print(x_dif, y_dif)
        # cv2.circle(frame, (x, y), 5, (255, 255, 255), -1)

        detections = sv.Detections.from_yolov8(result)
        # tracks = byte_tracker.update(frame.shape, detections)
        # print(tracks)
        # detections = match_detections_with_tracks(
        #     detections=detections, 
        #     tracks=tracks)
        # print(result)
        if result.boxes.id is not None:
            detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)
        # print(detections)
        labels = [
            f"#{tracker_id} {confidence:0.2f}"
            for _, _, confidence, class_id, tracker_id,
            in detections
        ]
        frame = box_annotator.annotate(
            scene=frame, 
            detections=detections,
            labels=labels
        )
        
        t3 = time.time()
        cv2.imshow("yolov8", frame)

        if (cv2.waitKey(30) == 27): # break with escape key
            break
        print("FPS: ", 1 / (time.time() - t), " S1: ", t1 - t, " S2: ", t2 - t1, " S3: ", t3 - t2)
            
    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
