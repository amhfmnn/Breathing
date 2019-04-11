from pipeline import PipeLine
import numpy as np
import cv2
from parameters import getParam

def sampleAndRunLoop(vidSource):

    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    if int(major_ver)  < 3 :
        fps = vidSource.get(cv2.cv.CV_CAP_PROP_FPS)
    else :
        fps = vidSource.get(cv2.CAP_PROP_FPS)

    if fps == 0:
        fps = 24

    sampleLen = getParam["SampleLength"]

    ret, frame = vidSource.read()
    sample = np.zeros(( sampleLen, frame.shape[0], frame.shape[1], 3 ), dtype=np.uint8)
    idx = 0

    pipeline = PipeLine(fps)

    while True:
        ret, frame = vidSource.read()
        
        if idx < sampleLen:
            sample[idx] = frame
            # continue
        else:
            # Slide sampling window
            sample = np.insert( sample[1:], -1, frame, axis = 0)
        print("Sampler: ")
        print(type(sample))
        # Perform computation of frequency
        respiratoryRate = pipeline.run(sample)
        print(respiratoryRate)
        idx += 1

        # Display result on the output image
        cv2.putText(frame, "Frame: %d, %d bps"%(idx, respiratoryRate), (50,50), cv2.FONT_HERSHEY_TRIPLEX, 0.7, (0,20,255))
        r = cv2.rectangle(frame, (400, 700), (900, 1080), (100, 50, 200), 5)

        cv2.imshow('output', r)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
 

