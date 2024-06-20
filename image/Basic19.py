# Demo เเสดงภาพสีจากจุด Pixel
# การกำนหดรูปภาพรูปทรงใน project

import cv2
import numpy
img = numpy.zeros([400,400,3]) #สร้างภาพสีดำ

points = []

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN or 0xFF == ('e'):
        #cv2.cricle(เเสดงภาพ,พิกัด,สีของเส้น,ขนาดของเส้น)
        cv2.circle(img,(x,y),5,(0,124,244),4)
        #สร้างตำเเหน่งทั้งสองจุด
        points.append((x,y))
        print(points)
        #ถ้าามีจุดมากกว่าสองจุดให้เขียนเส้นมาเชื่อมจุด
        if len(points) >= 2: 
           cv2.line(img,points[-2],points[-1],(0,255,0),4)
        
        cv2.imshow("Output",img)
        

#เเสดงภาพ
cv2.imshow("Output",img)

#เเชื่องโยงกับ Mouse
cv2.setMouseCallback("Output",clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()