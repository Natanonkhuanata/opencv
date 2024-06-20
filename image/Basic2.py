# การอ่านภาพ
# การเเสดงผลภาพ

import cv2

#การอ่านภาพ
img = cv2.imread("image/Robot.jpg")


#การเเสดงภาพ
cv2.imshow("title",img) #การเเสดงภาพ tile and live photograp
cv2.waitKey(0) #เวลา 1 วิ จะะออก
cv2.destroyAllWindows() #คืนทรัพยากรสู่ที่เดิม