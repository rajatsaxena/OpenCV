import numpy as np
import cv2

img = cv2.imread('7.png')

ball=img[50:80, 100:180]
img[90:120, 0:80]=ball

cv2.imshow('image',img)
k = cv2.waitKey(0) % 0xFF
if k == 27:
	# wait for ESC key to exit
	cv2.destroyAllWindows()
