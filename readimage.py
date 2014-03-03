import numpy as np
import cv2

img= cv2.imread('rajat.JPG',0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('img', img)
k=cv2.waitKey(0) % 0xFF   #for a 64 bit system
if k==27:    #wait for ESC key to exit
	cv2.destroyAllWindows()
elif k==ord('s'):    #checks if s is pressed
	cv2.imwrite('rajatgrey.png',img)  
	cv2.destroyAllWindows()
