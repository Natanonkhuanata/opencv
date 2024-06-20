#ตรวจจับวัตถุกลุ่มสี

import cv2
import numpy

while True:
    img = cv2.imread("image/ball2d01.jpg")
    img = cv2.resize(img,(400,400))

    # มีภาพสีเเขียวอยู่เท่าไหร่
    upper = numpy.array([124,255,133])
    lower = numpy.array([5,111,10])
    
    mask = cv2.inRange(img,lower,upper)

    mask = cv2.inRange(img,lower,upper) #
    Result = cv2.bitwise_and(img,img,mask=mask)
    if cv2.waitKey(0) & 0xFF == ord('e'):
        break

    cv2.imshow("Original",img)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",Result)

cv2.destroyAllWindows()