import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
	print("I don't want to open camera")
	exit()

while True:
	ret, frame = cap.read()
	if not ret:
		print("Can't see")
		break
	# Go to hsv color space
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	# Create blue range
	lower_blue = np.array([100,150,0])
	upper_blue = np.array([140,255,255])

	# Get binary mask with blue detected
	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	# Close, dilate-erode and open erode-dilate to clean image
	kernel_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
	kernel_open = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_close)
	openning = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel_open)

	img = openning

	# calculate moments of binary image
	M = cv2.moments(img)
	
	# calculate x,y coordinate of center
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
	
	# put text and highlight the center
	cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
	cv2.circle(frame, (int(frame.shape[1] / 2), int(frame.shape[0] / 2)), 5, (255, 255, 0), -1)
	# cv2.putText(frame, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	x_dif = cX - frame.shape[1] / 2
	y_dif = cY - frame.shape[0] / 2
	print(x_dif, cX, y_dif, cY)
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
