import cv2
import numpy as np

def doNothing(x): pass

cv2.namedWindow('trackbar')

cap = cv2.VideoCapture(0)

cv2.createTrackbar('Hue Lower','trackbar',0,255,doNothing)
cv2.createTrackbar('Saturation Lower','trackbar',0,255,doNothing)
cv2.createTrackbar('Value Lower','trackbar',0,255,doNothing)

cv2.createTrackbar('Hue Higher','trackbar',255,255,doNothing)
cv2.createTrackbar('Saturation Higher','trackbar',255,255,doNothing)
cv2.createTrackbar('Value Higher','trackbar',255,255,doNothing)

while True:
    # img = cv2.imread('download.jpeg')
    _,img = cap.read()
    img = cv2.flip(img,1)

    hsv_image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('Hue Lower','trackbar')
    l_s = cv2.getTrackbarPos('Saturation Lower', 'trackbar')
    l_v = cv2.getTrackbarPos('Value Lower', 'trackbar')

    h_h = cv2.getTrackbarPos('Hue Higher', 'trackbar')
    h_s = cv2.getTrackbarPos('Saturation Higher', 'trackbar')
    h_v = cv2.getTrackbarPos('Value Higher', 'trackbar')

    l_bound = np.array([l_h,l_s,l_v])
    u_bound = np.array([h_h,h_s,h_v])


    mask = cv2.inRange(hsv_image,l_bound,u_bound)

    res = cv2.bitwise_and(img,img,mask=mask)

    if cv2.waitKey(1) == ord('q'): break;

    cv2.imshow('mask',mask)
    cv2.imshow('original image',img)
    cv2.imshow('image',res)


cap.release()
cv2.destroyAllWindows()