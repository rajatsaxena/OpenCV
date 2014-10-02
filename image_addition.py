#opencv addition is saturated operation
#numpy addition is modulo operation

import cv2
import numpy as np

x=np.uint8([250])
y=np.uint8([10])

print cv2.add(x,y) # 250 + 10 = 260 => 255

print x + y # 260 % 256 => 4


