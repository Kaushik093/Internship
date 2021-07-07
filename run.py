from WritingNew import utils
import cv2

wCam, hCam = 610, 470

capture = cv2.VideoCapture(0)
capture.set(3, wCam)
capture.set(4, hCam)

while True:
    ret, image = capture.read()

    if not ret:
        capture.release()
        cv2.destroyAllWindows()
        break

    image = utils.get(image)

    cv2.imshow('Detecting', image)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        cv2.destroyAllWindows()
        break