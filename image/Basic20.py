#ตรวจจับวัตถุกลุ่มสี

import cv2
import numpy

while True:
    img = cv2.imread("image/ball2d.jpg")
    img = cv2.resize(img,(400,400))

    # มีภาพสีเเขียวอยู่เท่าไหร่
    upper = numpy.array([96,255,123])
    lower = numpy.array([4,105,7])

    
