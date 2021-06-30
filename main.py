import cv2

#import Take_pic as pic

img=cv2.imread("Images/obj88.jpg")

# img=cv2.resize(img,(0,0),fx=0.1,fy=0.1)
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


    if (len(approx) == 4):
        cv2.putText(img, "Rectangle/square",(x,y), font, 1, (0))


cv2.imshow("output",img)
# cv2.imshow("threshold",img_thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()