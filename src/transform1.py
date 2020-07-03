
from transform import four_point_transform
import numpy as np
import argparse
import os
import cv2
# construct the argument parse and parse the arguments
"""ap = argparse.ArgumentParser()
#--image B:\example_01.png --coords "[(63, 242), (291, 110), (361, 252), (78, 386)]"
ap.add_argument("-i", "--image", help = "B:\example_01.png")
ap.add_argument("-c", "--coords",
	help = "[(63, 242), (291, 110), (361, 252), (78, 386)]"
args = vars(ap.parse_args())"""
# load the image and grab the source coordinates (i.e. the list of
# of (x, y) points)
# NOTE: using the 'eval' function is bad form, but for this example
# let's just roll with it -- in future posts I'll show you how to
# automatically determine the coordinates without pre-supplying them
'''
path = "example_01.jpg"
if os.path.isfile(path):
    img1 = cv2.imread(path, 0)
else:
    print ("The file " + path + " does not exist.")

'''
'''
width 300
height 168
'''
image = cv2.imread("B:\ex.jpg")
 
pts = np.array([(55, 0), (170, 0), (170,60), (0, 70)], dtype = "float32")
# apply the four point tranform to obtain a "birds eye view" of
# the image
warped = four_point_transform(image, pts)
# show the original and warped images
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)
