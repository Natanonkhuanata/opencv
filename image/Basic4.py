# การกำหนดรูปแบบภาพ
# การอ่านภาพ
# การเเสดงผลภาพ

import cv2

#การอ่านภาพ
img = cv2.imread("image/Robot.jpg",1)  # 0 = gray scle หรือขาวดำ  /  1 = RGB หรือภาพสีเเบบเดิม  / -1 = RGB aufa หรือ การเเบบเเอลฟา
                                       


#การเเสดงภาพ
cv2.imshow("title",img) #การเเสดงภาพ tile and live photograp
cv2.waitKey(delay=1000) #เวลา 1 วิ จะะออก
cv2.destroyAllWindows() #คืนทรัพยากรสู่ที่เดิม