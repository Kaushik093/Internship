import cv2
import time

wCam, hCam = 500, 370

capture = cv2.VideoCapture(0)
capture.set(3, wCam)
capture.set(4, hCam)
pTime = 0
count = 0

while True:

    ret, img = capture.read()

    if not ret:
        capture.release()
        cv2.destroyAllWindows()
        break


    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
    _,img_thresh=cv2.threshold(img_blur,210,255,cv2.THRESH_BINARY)
    contours,hierarchy=cv2.findContours(img_thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    font=cv2.FONT_HERSHEY_COMPLEX

    for contour in contours:
        approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
        cv2.drawContours(img,approx,-1,(0,0,0),5)

        x=approx.ravel()[0]
        y=approx.ravel()[1]

        print(approx)

        if (len(approx) == 4):
            cv2.putText(img, "Rectangle/square",(x,y), font, 1, (0))

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)) + " fps", (10, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

    cv2.imshow("output",img)
    if cv2.waitKey(20) & 0xFF == ord('d'):
            break


cv2.waitKey(0)
cv2.destroyAllWindows()