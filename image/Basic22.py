# ตรวจจับใบหน้าจากวิดีโอ



import cv2

#อ่านวิดีโอ
cap = cv2.VideoCapture("imgae/Mark.mp4")

while(cap.isOpened):
    check , frame = cap.read()   #อ่านวิดีโอ โดยเก็บในตัวแปร check
    if check == True:
       cv2.imshow("Output",frame)
       if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

#เเสดงผล