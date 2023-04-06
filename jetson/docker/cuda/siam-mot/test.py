import cv2
import os

print("file exists?", os.path.exists('video.mp4'))
video = cv2.VideoCapture('video.mp4')

frame_count = 0

if not video.isOpened():
    print("no open")

while True:
    # Read the next frame from the video
    ret, frame = video.read()
    print(frame)
    # If the frame could not be read, break out of the loop
    if not ret:
        if (frame):
            print("frame")
        print("not ret")
        break
    frame_count += 1
    # Display the frame (optional)

print(frame_count)
# Release the video capture object and close any windows
video.release()
