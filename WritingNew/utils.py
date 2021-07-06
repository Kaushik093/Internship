import cv2
import numpy as np

def get(img):
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.GaussianBlur(grey, (5, 5), 1)