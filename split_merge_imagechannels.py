import cv2
import numpy as np

img=cv2.imread('rajat.jpg')

b,g,r=cv2.split(img)  #used to split 
img=cv2.merge((b,g,r)) #used to merge channels
