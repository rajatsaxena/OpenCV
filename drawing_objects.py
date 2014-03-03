#cv2.line(), cv2.circle(), cv2.rectangle(), cv2.ellipse(), cv2.putText(

import numpy as np
import cv2

#create blank image
img=np.zeroes((512,512,3), np.uint8)

#diagonal blue line with thickness of 5 pixels using 2 coordinates
img = cv2.line(img, (0,0), (511,511), (255,0,0), 5)

#green rectangle at top-right corner of image using top-left and bottom -right corner
img = cv2.rectangle(img, (384,0), (510,128), (0,255,0), 3)

#drawing circle using center coordinates and radius. 
img = cv2.circle(img, (447,63), 63, (0,0,255), -1)

#drawing ellipse requires center location, axis length, angle of rotation in anti clockwise order.
img = cv2.ellipse(img,(256,256), (100,50),0,0,180,255,-1)

#drawing a polygon you need coordinates of vertices. a polygom with 4 vertices in yellow color.
pts=np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
pts=pts.reshape((-1,1,2))
img=cv2.polylines(img, [pts], True, (0,255,255))

#if third argument is false u will get polylines joining all points not a closed shape

 
