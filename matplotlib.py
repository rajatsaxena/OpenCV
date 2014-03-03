import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('rajat.jpg',0)
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.xticks([]), plt.yticks([]) #to hide tick values on X and Y axis
plt.show()

#color image loaded by opencv is in BGR mode. but matplotlib displays in RGB mode. So color images will not be displayed correctly in Matplotlib if image is read with OpenCV. 


