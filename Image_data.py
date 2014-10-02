from PIL import Image
import numpy
from pylab import *

im=array(Image.open('1.png'))
print im.shape, im.dtype

im=array(Image.open('1.png').convert('L'),'f')
print im.shape, im.dtype
