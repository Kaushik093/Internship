import cv2
import numpy as np


def get(img, filter = 0):
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (5, 5), 1)
    canny = cv2.Canny(blur, 100, 100)
    kernel = np.ones((5, 5))
    dilate = cv2.dilate(canny, kernel=kernel, iterations=3)
    erode = cv2.erode(dilate, kernel, iterations=2)

    minarea = 10000
    finalContour = []

    contours, heirarchy = cv2.findContours(
        erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

        if area > minarea:
            bbox = cv2.boundingRect(approx)

            if filter > 0:
                if(len(approx) == filter):
                    finalContour.append([len(approx)], area, approx, contour)

        else:
            finalContour.append([len(approx), area, approx, contour])
        
        finalContour = sorted(finalContour, key=lambda x:x[1], reverse=True)
        
        for con in finalContour:
            cv2.drawContours(img, contour, -1, (0, 0, 255), 3)
    
    return img, finalContour
