import sys
import cv2
from sampler import *
import os

filename = ('vid_1.mp4')
cap = cv2.VideoCapture(filename)


#if len(sys.argv) > 1:
#    cap = cv2.VideoCapture(sys.argv[1])
#else:
#    cap = cv2.VideoCapture(0)

ret, frame = cap.read()
cv2.imshow('im', frame)
sampleAndRunLoop(cap)

cap.release()
cv2.destroyAllWindows()
