#การวาดภาพลงใน project

import cv2


#การอ่านภาพ

img = cv2.imread("image/Robot.jpg")


#การกำหนดขนาดของภาพ

imresize = cv2.resize(img,(700,700))



# การวาดสี่เหลี่ยมลงบนภาพ
# rectangle(ภาพ,มุมที่ 1 (บนซ้าย),มุมที่ 2 (ล่างขวา),สี,ความหนา)

cv2.rectangle(imresize,(200,200),(400,400),(0,0,255),5)

cv2.imshow("Output",imresize)
cv2.waitKey()
cv2.destroyAllWindows() 