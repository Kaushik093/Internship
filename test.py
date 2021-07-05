import cv2
import time
import numpy as np
from matplotlib import pyplot as plt

wCam, hCam = 510, 370

capture = cv2.VideoCapture('clips/box1.mp4')
capture.set(3, wCam)
capture.set(4, hCam)
pTime = 0
count = 0
x = 0.0
y = 0.0

while True:
    ret, img = capture.read()

    if not ret:
        capture.release()
        cv2.destroyAllWindows()
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    thresh_inv = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]

    # Blur the image
    blur = cv2.GaussianBlur(thresh_inv, (1, 1), 0)

    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

    # find contours
    contours = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    mask = np.ones(img.shape[:2], dtype="uint8") * 255
    for c in contours:
        # get the bounding rect
        x, y, w, h = cv2.boundingRect(c)
        if 1000 < w*h < 100000:
            cv2.rectangle(mask, (x, y), (x+w, y+h), (0, 0, 255), -1)

    img = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)) + " fps", (10, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)


    cv2.imshow("boxes", mask)
    cv2.imshow("final image", img)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        cv2.destroyAllWindows()
        break
