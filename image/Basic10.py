#การวาดภาพลงใน project

import cv2


#การอ่านภาพ

img = cv2.imread("image/Robot.jpg")


#การกำหนดขนาดของภาพ

imresize = cv2.resize(img,(700,700))



#การวาดเส้นตรง
#arrowedLine  คือการใส่หัวลูกศร
# line (ภาพ , จุดเริ่มต้น(x,y), จุดสุดท้าย(x,y), สี (BGR) ,ความหนา)
cv2.line(imresize,(0,0),(100,100),(255,0,0),10)


cv2.imshow("Output",imresize)
cv2.waitKey()
cv2.destroyAllWindows()