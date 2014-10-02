from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

im = array(Image.open('1.png'))
im2 = zeros(im.shape)
for i in range(3):
	im2[:,:,i] = filters.gaussian_filter(im[:,:,i],5)
im2 = uint8(im2)
imshow(im2)
show()
