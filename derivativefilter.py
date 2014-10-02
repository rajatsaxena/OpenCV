from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

im = array(Image.open('1.png').convert('L'))

#Sobel derivative filters
imx = zeros(im.shape)
filters.sobel(im,1,imx)
imshow(imx)
show()

imy = zeros(im.shape)
filters.sobel(im,0,imy)
imshow(imy)
show()

magnitude = sqrt(imx**2+imy**2)
imshow(magnitude)
show()

#gaussianderivative
sigma = 5 #standard deviation

imx = zeros(im.shape)
filters.gaussian_filter(im, (sigma,sigma), (0,1), imx)

imy = zeros(im.shape)
filters.gaussian_filter(im, (sigma,sigma), (1,0), imy)
