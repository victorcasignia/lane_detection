import numpy as np
import cv2
import glob
import os.path

def calibrate(location, row, col):

	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

	objp = np.zeros((row*col,3), np.float32)
	objp[:,:2] = np.mgrid[0:col,0:row].T.reshape(-1,2)

	objpoints = [] 
	imgpoints = []

	images = glob.glob(location + '*.jpg')
	for fname in images:
		img = cv2.imread(fname)
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		ret, corners = cv2.findChessboardCorners(gray, (col,row), None)
		if ret == True:
			objpoints.append(objp)
			corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
			imgpoints.append(corners2)

	ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
	return ret, mtx, dist, rvecs, tvecs;

def undistort(img, mtx, dist):
	h,  w = img.shape[:2]
	newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
	
	dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

	x,y,w,h = roi
	dst = dst[y:y+h, x:x+w]
	return dst;


ret, mtx, dist, rvecs, tvecs = calibrate("data/camera_cal/", 6, 9)

img = cv2.imread("data/camera_cal/calibration4.jpg")

ds = undistort(img, mtx, dist)

cv2.imshow('img',ds)
cv2.waitKey(0)
