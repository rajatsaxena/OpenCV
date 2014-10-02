from PIL import Image
from pylab import *

def compute_average(imlist):
	""" Compute the average of a list of images. """
	# open first image and make into array of type float
	averageim = array(Image.open(imlist[0]), 'f')
	for imname in imlist[1:]:
		try:
			averageim += array(Image.open(imname))
		except:
			print imname + '...skipped'
	averageim /= len(imlist)
	
	# return average as uint8
	return array(averageim, 'uint8')

im1 = array(Image.open('1.png').convert('L'))
im2= array(Image.open('2.png').convert('L'))
im=[im1,im2]
im3= compute_average(im1)
imshow(im3)
show()
