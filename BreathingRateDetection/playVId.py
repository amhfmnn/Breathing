import numpy as np
import cv2 as cv
import os

filename = ("vid_1.mp4")
cap = cv.VideoCapture('vid_1.mp4')
while(cap.isOpened()):
    ret, frame = cap.read()
    print(type(frame))
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()