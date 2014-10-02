from PIL import Image
from numpy import *
from pylab import *

im=array(Image.open('f.png').convert('L'))
imshow(im)
show()
im2=255-im #invert image
imshow(im2)
show()
im3= (100.0/255)*im + 100 #clamp to interval 100...200
imshow(im3)
show()
im4= 255.0 * (im/255.0)**2 #squared
imshow(im4)
show()

