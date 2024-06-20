#การวาดภาพลงใน project

import cv2


#การอ่านภาพ

img = cv2.imread("image/Robot.jpg")


#การกำหนดขนาดของภาพ

imgresize = cv2.resize(img,(700,700))



#การวาดวงกลม
# line (ภาพ ,ตำเเหน่งจุดศูนย์กลางวงกลม ,(x,y),รัศมี,สี (BGR),ความหนา)

cv2.circle(imgresize,(350,400),100,(0,255,0),2)

cv2.imshow("Output",imgresize)
cv2.waitKey()
cv2.destroyAllWindows()