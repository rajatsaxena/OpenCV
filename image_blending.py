import cv2
import numpy as np

img1=cv2.imread('ml.png')
img2=cv2.imread('opencv_logo.jpg')

dst=cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshoe('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


