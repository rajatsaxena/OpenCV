import warp
import matplotlib.delaunay as md 
from scipy import ndimage
from pylab import *
from numpy import *
from PIL import Image

im1 = array(Image.open('1.png').convert('L'))
im2 = array(Image.open('2.png').convert('L'))

tp = array([[264,538,540,264],[40,36,605,605],[1,1,1,1]])

im3 = warp.image_in_image(im1,im2,tp)
figure()
gray()
imshow(im3)
axis('equal')
axis('off')
show()
