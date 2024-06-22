#การเปิดวิดีโอ ด้วยopencv


import cv2

cap = cv2.VideoCapture("image/Robot.mp4") # ตรวจหาที่เก็บวิดีโอ

while(cap.isOpened):
    check , frame = cap.read()   #อ่านวิดีโอ โดยเก็บในตัวแปร check
    if check == True:
       cv2.imshow("Output",frame)
       if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()