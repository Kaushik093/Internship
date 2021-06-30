import cv2
import os

cap=cv2.VideoCapture(0)
frame_count=0

os.chdir('Images')

while(cap.isOpened()):
    ret,frame=cap.read()
    if(ret==False):
        break
    cv2.imwrite("obj"+str(frame_count)+'.jpg',frame)
    frame_count+=1
    if(frame_count==100):
        break
cap.release()
cv2.destroyAllWindows()