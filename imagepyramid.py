import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('7.png')
lower_reso = cv2.pyrDown(img)
higher_reso2 = cv2.pyrUp(lower_reso)
titles = ['Original Image', 'lower resolution','higher resolution']
images = [img, lower_reso, higher_reso2]
for i in xrange(3):
	plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])

plt.show()
