import cv2

def banana():
    path = 'haarcascade_banana.xml'
    camNo = 0
    objectname = 'Banana'
    framewidth = 640
    frameheight = 480
    color = (255, 0, 255)
    cap = cv2.VideoCapture(0)
    cap.set(3, framewidth)
    cap.set(4, frameheight)


    def empty(a):
        pass


    cv2.namedWindow("result")
    cv2.resizeWindow("result", framewidth, frameheight + 100)
    # cv2.createTrackbar("scale", "result", 400, 1000, empty)
    # cv2.createTrackbar("neig", "result", 8, 20, empty)
    # cv2.createTrackbar("min area", "result", 0, 100000, empty)
    # cv2.createTrackbar("brightness", "result", 180, 255, empty)

    cascade = cv2.CascadeClassifier(path)

    while True:
        # camBrightness = cv2.getTrackbarPos("brightness", "result")
        camBrightness=152
        cap.set(10, camBrightness)
        s, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # scaleval = 1 + (cv2.getTrackbarPos("scale", "result") / 1000)
        # neig = cv2.getTrackbarPos("neig", "result")
        objects = cascade.detectMultiScale(gray, 120, 5)
        for (x, y, w, h) in objects:
            area = w * h
            # minArea = cv2.getTrackbarPos("min area", "result")
            minArea=152
            if area > minArea:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                cv2.putText(img, objectname, (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)


        cv2.imshow("result", img)

        if cv2.waitKey(1) & 0XFF == ord('q'):
            cv2.destroyAllWindows()
            break