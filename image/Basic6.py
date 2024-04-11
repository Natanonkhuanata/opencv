#การเปิดกล้องด้สย opencv

import cv2

#การเปิดกล้อง
cap = cv2.VideoCapture(0)  #การระบุหมายเลขกล้อง
while (True):
    check , frame = cap.read()  #รับภาพจากกล้อง frame ต่อ frame
    cv2.imshow("Output",frame)

    if cv2.waitKey(1) & 0xFF ==  ord("e"):
       break

cap.release #คือทรัพยากร
cv2.destroyAllWindows() #คืนทรัพยากร 