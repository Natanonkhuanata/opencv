#การเปิดวิดีโอ ด้วยopencv
# Video gray scale


import cv2

cap = cv2.VideoCapture("image/Robot.mp4") # ตรวจหาที่เก็บวิดีโอ

while(cap.isOpened):
    check , frame = cap.read()   #อ่านวิดีโอ โดยเก็บในตัวแปร frame
    if check == True:
       gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
       cv2.imshow("Output",gray)
       if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()