import numpy as np
import cv2

def detect_black_areas(filename):
  m1 = cv2.imread(filename)
  m2 = cv2.cvtColor(m1, cv2.cv.CV_BGR2GRAY)
  m3 = 255 - cv2.threshold(m2, 0, 255, cv2.THRESH_OTSU)[1]
  m4 = cv2.distanceTransform(m3, cv2.cv.CV_DIST_L2, 3)
  m5 = cv2.normalize(m4, alpha=0., beta=1., norm_type=cv2.NORM_MINMAX)
  m6 = cv2.threshold(m5, .8, 1., cv2.THRESH_BINARY)[1]
  m7 = cv2.dilate(m6, np.ones((3,3), np.uint8), iterations=7)
  cnt = cv2.findContours(m7.astype(np.uint8), 
                           cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
  cv2.drawContours(m1, cnt, -1, (0,0,255), 2)
  cv2.imshow("image", m1)
  cv2.waitKey() % 0xFF

if __name__ == "__main__":
  files = ["KjTp9.png", "AuHP7.png", "jFkNM.png", "Yksk9.png"]
  for file in files:
    detect_black_areas(file)
