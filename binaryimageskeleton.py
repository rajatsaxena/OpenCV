from skimage import morphology
import cv2

im = cv2.imread("rajat.jpg")
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
im = cv2.threshold(im, 0, 255, cv2.THRESH_OTSU)[1]
im = morphology.skeletonize(im > 0)
cv2.imwrite("dst.png", im)
