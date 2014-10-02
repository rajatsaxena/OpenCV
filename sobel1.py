from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

im = array(Image.open('rajat.JPG').convert('L'))

#Sobel derivative filters
imx = zeros(im.shape)
filters.sobel(im,1,imx)

imshow(imx)
show()

imy = zeros(im.shape)
filters.sobel(im,0,imy)
magnitude = sqrt(imx**2+imy**2)

imshow(imy)
show()

imshow(magnitude)
show()
