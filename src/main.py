import calibrate

ret, mtx, dist, rvecs, tvecs = calibrate("data/camera_cal/", 6, 9)

img = cv2.imread("data/camera_cal/calibration4.jpg")

ds = undistort(img, mtx, dist)

cv2.imshow('img',ds)
cv2.waitKey(0)
