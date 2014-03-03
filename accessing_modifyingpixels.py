import cv2
import numpy as np

#access a pixel value by its row and col coordinates
#for BGR image, it returns Blur, Green and Red values
#for greyscale image, just corresponding intensity is returned

img=cv2.imread('rajat.jpg')

px=img[100,100]
print px

#accessing only blue pixel
blue=img[100,100,0]
print blue

#modifying pixel value
img[100,100]=[255,255,255]
print img[100,100]

#accessing red value
img.item(10,10,2)

#modifying red value
img.itemset((10,10,2),100)
img.item(10,10,2)



