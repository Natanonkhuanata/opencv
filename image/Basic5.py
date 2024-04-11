#การเขียนภาพ (Export)

# การกำหนดรูปแบบภาพ
# การอ่านภาพ
# การเเสดงผลภาพ

import cv2

#การอ่านภาพ
img = cv2.imread("image/Robot.jpg",0)
imgresize = cv2.resize(img,(500,600))
                                       


#การเเสดงภาพ
cv2.imshow("title",img) #การเเสดงภาพ tile and live photograp

#การเขียนภาพ
cv2.imwrite("Output.jpg",imgresize) #จะได้ภาพ Output.jpg ออกไปใช้งาน 
cv2.waitKey(delay=1000) #เวลา 1 วิ จะะออก
cv2.destroyAllWindows() #คืนทรัพยากรสู่ที่เดิม