import cv2

path = 'cascade\cascade.xml'
camNo = 1
objectname = 'Cup'
framewidth = 640
frameheight = 480
color = (255, 0, 255)

cap = cv2.VideoCapture(camNo)
cap.set(3, framewidth)
cap.set(4, frameheight)


def empty(a):
    pass


cv2.namedWindow("result")
# cv2.resizeWindow("result", framewidth, frameheight + 100)
# cv2.createTrackbar("scale", "result", 400, 1000, empty)
# cv2.createTrackbar("neig", "result", 8, 20, empty)
# cv2.createTrackbar("min area", "result", 0, 100000, empty)
# cv2.createTrackbar("brightness", "result", 180, 255, empty)
# scale value and neighbours

cascade = cv2.CascadeClassifier(path)
#Cascade classifier
while True:
    # camBrightness = cv2.getTrackbarPos("brightness", "result")
    camBrightness=180
    cap.set(10, camBrightness)
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # scaleval = 1 + (cv2.getTrackbarPos("scale", "result") / 1000)
    neig = cv2.getTrackbarPos("neig", "result")
    objects = cascade.detectMultiScale(gray, 308,12)
    #detectMultiScale
    for (x, y, w, h) in objects:
        area = w * h
        # minArea = cv2.getTrackbarPos("min area", "result")
        minArea=23318
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
            cv2.putText(img, objectname, (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)

    cv2.imshow("result", img)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break