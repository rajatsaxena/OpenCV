import numpy as np
import cv2

img= cv2.imread('rajat.jpg',0)
cv2.imshow('img', img)
k=cv2.waitKey(0) & 0xFF
if k==27:    #wait for ESC key to exit
	cv2.destroyAllWindows()
elif k==ord('s'):
	cv2.imwrite('rajatgrey.png',img)
	cv2.destroyAllWindows()n
