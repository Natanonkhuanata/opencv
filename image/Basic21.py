#ตรวจจับใบหน้าจากรูปภภาพ  (face delection)

import cv2

#อ่านภาพ
img = cv2.imread("image/Love.jpg")
imgresize = cv2.resize(img,(600,600))
img = cv2.imread("image/NINJA.jpg")
imgresize = cv2.resize(img,(600,700))
face_cascade = cv2.CascadeClassifier("image/Detect/haarcascade_frontalface_default.xml") #การอ้านไฟล์สำหรับ cassification

gray_img = cv2.cvtColor(imgresize,cv2.COLOR_BGR2GRAY)   #ทำให้ภาพเบลอด้วย grayscale

#จำเเนกใบหน้า
scaleFactor = 1.1 #ทำการ Redult สัดส่วนของภาพ
minNeighbors = 5  #ค่าที่ใช้ตีรวจสอบของ grayscale
face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighbors)

#เเสดงภาพใบหน้า
for (x,y,w,h) in face_detect:
      cv2.rectangle(imgresize,(x,y),(x+w,y+h),(0,255,0),thickness=5)

#เเสดงภาพ
cv2.imshow("Original",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()

