import sift
from PIL import Image
from numpy import *
from pylab import *

imname = '1.png'
im1 = array(Image.open(imname).convert('L'))
sift.process_image(imname,'empire.sift')
l1,d1 = sift.read_features_from_file('empire.sift')
figure()
gray()
sift.plot_features(im1,l1,circle=True)
show()
