import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Can't open camera")
    exit()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('Webcam', frame)

    # Exit if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()