from PIL import Image
from numpy import *
from pylab import *

def histeq(im,nbr_bins=256):
	# get image histogram
	imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
	cdf = imhist.cumsum() # cumulative distribution function
	cdf = 255 * cdf / cdf[-1] # normalize
	# use linear interpolation of cdf to find new pixel values
	im2 = interp(im.flatten(),bins[:-1],cdf)
	return im2.reshape(im.shape), cdf


im = array(Image.open('f.png').convert('L'))

imshow(im)
show()
figure()
hist(im.flatten(),128)
show()


im2,cdf = histeq(im)

imshow(im2)
show()
figure()
hist(im2.flatten(),128)
show()
