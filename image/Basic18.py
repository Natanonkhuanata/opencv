#เเสดงภาพสีจากจุด  pixel


import cv2
import numpy

img = cv2.imread("image/Robot.jpg")

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN or 0xFF == ('e'):
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        imgcolor = numpy.zeros([300,300,3],numpy.uint8)#กำหนดความกว้าง ความสูง ความยาว
        imgcolor[:] = [blue,green,red]
        print(imgcolor)
        cv2.imshow("Result",imgcolor) #เเสดงภาพสีจากรูปภาพใน tite ของ Result

#เเสดงภาพ
cv2.imshow("Output",img)

#เชื่อมกับ Mouse
cv2.setMouseCallback("Output",clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()
