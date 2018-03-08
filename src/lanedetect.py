import cv2
import numpy as np

#algo
#
#1. filter traffic lanes
#	-convert to hsl
#	-smoothen image
#	-get white and yellow lanes
#	-otsu threshold the S
#	-hough lines
#2. find ROI
#	-find longest line in N frames
#	-use end point as y boundary
#	-check if line start point is right or left of the middle point
#	-find the next line to its opposite side within M frames
#	-project the shorter line to match longer line height
#	-use the two lines to generate trapezoid area 
#	-if area is not generated, repeat ROI search
#	

def filterYellowWhiteLane(img):
	image = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
	#blur and dilate
	image = cv2.GaussianBlur(image,(9,9),0)

	#get yellow and white
	lower = np.uint8([  0, 200,   0])
	upper = np.uint8([255, 255, 255])
	white_mask = cv2.inRange(image, lower, upper)
	lower = np.uint8([ 10,   0, 100])
	upper = np.uint8([ 40, 255, 255])
	yellow_mask = cv2.inRange(image, lower, upper)
	mask = cv2.bitwise_or(white_mask, yellow_mask)
	image = cv2.bitwise_and(image, image, mask = mask)

	#use S and threshold
	h,l,s = cv2.split(image)
	ret,thresh1 = cv2.threshold(s,200,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	return thresh1;

def findLongestLine(img):
	return;
