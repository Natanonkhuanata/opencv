import cv2

#อ่านภาพ

img = cv2.imread("image/Robot.jpg")

# การกำหนดขนาด
imgresize = cv2.resize(img,(700,700))

# วาดภาพบนข้อความ
# putText(ภาพ,ข้อความ,พิกัดที่จะเเสดงข้อความ (x,y),font,ขนาดข้อความ,Color,ความหนา)
cv2.putText(imgresize,"Robot",(100,100),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,0,0),cv2.LINE_4)


cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()