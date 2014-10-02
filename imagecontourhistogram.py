from PIL import Image
from pylab import *

#read image to array
im = array(Image.open('1.png').convert('L'))

#create a new figure
figure()
#dont use a colors
gray()
#show contours with origin upper left corner
contour(im, origin='image')
axis('equal')
axis('off')

figure()
hist(im.flatten(),128)
show()