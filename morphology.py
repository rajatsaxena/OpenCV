from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *
from scipy.ndimage import measurements,morphology
# load image and threshold to make sure it is binary

im = array(Image.open('1.jpg').convert('L'))
im = 1*(im<128)

# morphology - opening to separate objects better
im_open = morphology.binary_opening(im,ones((9,5)),iterations=2)
labels_open, nbr_objects_open = measurements.label(im_open)
print "Number of objects:", nbr_objects_open