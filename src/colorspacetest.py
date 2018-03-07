import cv2
import numpy as np


def displayImage(img):
	b,g,r = cv2.split(img)
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	h,s,v = cv2.split(img)
	hsl = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
	h1,l,s1 = cv2.split(img)
	row1 = np.hstack((b,g,r))
	row2 = np.hstack((h,s,v))
	row3 = np.hstack((h1,l,s1))
	full = np.vstack((row1,row2, row3))
	unsplit = np.vstack((img, hsv, hsl))
	return full, unsplit;



cap = cv2.VideoCapture('data/video/project_video.mp4')

if (cap.isOpened()== False): 
	print("Error opening video stream or file")

while(cap.isOpened()):
	ret, frame = cap.read()
	if ret == True:
 	
		split, unsplit = displayImage(frame)
		resized = cv2.resize(unsplit, (960, 540))  
		cv2.imshow('output',resized)
 
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break

	else: 
		break
 
cap.release()
 
cv2.destroyAllWindows()


