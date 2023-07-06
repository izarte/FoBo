import cv2
import supervision as sv
from ultralytics import YOLO
import time
# from bytetracker import BYTETracker


def main():
    # define resolution
    cap = cv2.VideoCapture(0)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # specify the model
    model = YOLO("yolov8n.pt")
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
        # result = model(frame, agnostic_nms=True, device=0, classes=0)[0]
    # for result in model.track(source=0, stream=True, agnostic_nms=True, show=False, device=0, classes=0, tracker="bytetrack.yaml"):
        result = model.track(
            source=frame,
            # agnostic_nms=True,
            classes=0,
            device=0,
            # format='onnx',
            # tracker="bytetrack.yaml",
            half=True,
            verbose=False,
        )[0]
        print(result.boxes)
        print(result.masks)
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
        print(x_dif, y_dif)
        cv2.circle(frame, (x, y), 5, (255, 255, 255), -1)

        detections = sv.Detections.from_yolov8(result)
        # tracks = byte_tracker.update(frame.shape, detections)
        # print(tracks)
        # detections = match_detections_with_tracks(
        #     detections=detections, 
        #     tracks=tracks)
        # print(result)
        if result.boxes.id is not None:
            detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)
        labels = [
            f"#{tracker_id} {model.model.names[class_id]} {confidence:0.2f}"
            for _, _, confidence, class_id, tracker_id,
            in detections
        ]
        frame = box_annotator.annotate(
            scene=frame, 
            detections=detections, 
            labels=labels
        )
        
        cv2.imshow("yolov8", frame)

        if (cv2.waitKey(30) == 27): # break with escape key
            break
        print("FPS: ", 1 / (time.time() - t))
            
    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()