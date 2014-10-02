import cv2
import numpy as np

def nothing(x):
	pass

#blank image, a window
img=np.zeroes((300,512,3), np.uint8)
cv2.namedWindow('image')

#create trabar for color image
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

#switch for ON/OFF functionality
switch='0: OFF\n 1:ON'
cv2.createTrackbar(switch, 'image', 0,1,nothing)

while(1):
	cv2.imshow('image',img)
	k=cv2.waitKey(1) & 0xFF
	if k==27:
		break
	
	#current position of four trackers
	r=cv2.getTrackerPos('R','image')
	g=cv2.getTrackerPos('G','image')
	b=cv2.getTracekrPos('B','image')
	s=cv2.getTrackerPos(switch,'image')

	if s==0:
		img[:]=0
	else:
		img[:]=[b,g,r]

cv2.destroyAllWindows()

