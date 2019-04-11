import numpy as np
import cv2
import os

filename = ("vid_1.mp4")
cam_capture = cv2.VideoCapture('vid_1.mp4')

cv2.destroyAllWindows()

upper_left = (400, 700)
bottom_right = (900, 1080)

while True:
    _, image_frame = cam_capture.read()

    # Rectangle marker
    r = cv2.rectangle(image_frame, upper_left, bottom_right, (100, 50, 200), 5)
    rect_img = image_frame[upper_left[1]: bottom_right[1], upper_left[0]: bottom_right[0]]
    print(rect_img.shape)
    sketcher_rect = rect_img

    # Conversion for 3 channels to put back on original image (streaming)
    #sketcher_rect_rgb = cv2.cvtColor(sketcher_rect, cv2.COLOR_GRAY2RGB)

    # Replacing the sketched image on Region of Interest
    #image_frame[upper_left[1]: bottom_right[1], upper_left[0]: bottom_right[0]] = sketcher_rect_rgb

    cv2.imshow("Sketcher ROI", r)
    if cv2.waitKey(1) == 13:
        break

cam_capture.release()
cv2.destroyAllWindows()