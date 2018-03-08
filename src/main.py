import calibrate
import lanedetect
import cv2

ret, mtx, dist, rvecs, tvecs = calibrate.calibrate("data/camera_cal/", 6, 9)

cap = cv2.VideoCapture('data/video/project_video.mp4')

if (cap.isOpened()== False): 
	print("Error opening video stream or file")

while(cap.isOpened()):
	ret, frame = cap.read()
	if ret == True:
 	
		ds = calibrate.undistort(frame, mtx, dist)
		ds = lanedetect.filterYellowWhiteLane(ds)
		resized = cv2.resize(ds, (960, 540))  
		cv2.imshow('output',resized)
 
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break

	else: 
		break
 
cap.release()
 
cv2.destroyAllWindows()
