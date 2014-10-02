from PIL import Image
from numpy import *
from pylab import *

def imresize(im,sz):
	pil_im=Image.fromarray(uint8(im))
	
	return array(pil_im.resize(sz))

im=array(Image.open('1.png'))
im2=imresize(im,1020)
