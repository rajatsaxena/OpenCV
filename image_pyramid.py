import numpy as np
import cv2
#from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg')
lower_reso = cv2.pyrDown(higher_reso)

cv2.imshow('img', lower_reso)
cv2.destroyAllWindows()
