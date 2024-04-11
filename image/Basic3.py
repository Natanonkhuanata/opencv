#การอ่านภาำ
#การเเสดงผลภาพ
#การปรับขนาดภาพ

import cv2
#การอ่านภาพ
img = cv2.imread("image/Robot.jpg")

#การปรับขนาดภาพ
imresize = cv2.resize(img,(600,4000)) #การปับขนาดภาพพ wight * leight

#การเเสดงภาพ
cv2.imshow("title",imresize) #การเเสดงภาพ
cv2.waitKey(0) #เวลาในการเเสดงภาพ
cv2.destroyAllWindows()
