import cv2
import time


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Can't open camera")
    exit()

while True:
    # Read a frame from the camera
    t = time.time()
    ret, frame = cap.read()

    cv2.line(frame, (frame.shape[1] // 2, 0), (frame.shape[1] // 2, frame.shape[0]), (0, 255, 0), thickness=2)
    cv2.line(frame, (frame.shape[1] // 2, frame.shape[0] // 2), (frame.shape[1], 0), (0, 255, 255), thickness=2)
    cv2.line(frame, (frame.shape[1] // 2, frame.shape[0] // 2), (frame.shape[1], frame.shape[0]), (0, 255, 255), thickness=2)
    cv2.line(frame, (frame.shape[1] // 2, 0), (frame.shape[1], frame.shape[0]), (255, 255, 0), thickness=2)


    # Display the frame
    cv2.imshow('Webcam', frame)

    # Exit if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break
    print("FPS: ", 1 / (time.time() - t))

# Release resources
cap.release()
cv2.destroyAllWindows()