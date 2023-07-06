import cv2
import numpy as np
import math

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

	# Find the contours in the binary mask
	contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	# Sort the contours in descending order of their area
	contours = sorted(contours, key=cv2.contourArea, reverse=True)

	if len(contours) > 0:
		# Get the minimum bounding rectangle for the largest contour
		x, y, w, h = cv2.boundingRect(contours[0])

		# Draw the bounding box on the original image
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

		x += int(w / 2)
		y += int(h / 2)
		# put text and highlight the center
		cv2.circle(frame, (x, y), 5, (255, 255, 255), -1)
		cv2.circle(frame, (int(frame.shape[1] / 2), int(frame.shape[0] / 2)), 5, (255, 255, 0), -1)
		# cv2.putText(frame, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
		x_dif = x - frame.shape[1] / 2
		y_dif = y - frame.shape[0] / 2
		# 40 cm is w: 330 h: 192, area: 63360 hypotenuse: 381.79
		# distance1 = - (0.000130423) * (w * h) + 48.26
		distance2 = 381.79 * 40 / math.sqrt(w**2 + h**2)
		# print(f"center: {x} {y}, width: {w} height: {h} area: {w * h} hypotenuse: {math.sqrt(w**2 + h**2)}")
		# print(f"distance_area = {distance1} \t******\t distance_hypotenuse = {distance2}")
		print("distance: ", math.sqrt(w**2 + h**2))
	cv2.imshow('frame', frame)
	cv2.imshow('mask', openning)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()