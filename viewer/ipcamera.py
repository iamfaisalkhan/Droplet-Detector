from pymba import *
import time
import sys

# ID = int(sys.argv[1])

with Vimba() as vimba:
  system = vimba.getSystem()

  if system.GeVTLIsPresent:
    system.runFeatureCommand("GeVDiscoveryAllOnce")
    time.sleep(0.2)

  cameraIds = vimba.getCameraIds()

  for cameraId in cameraIds:
    print(cameraId)

    # camera0 = vimba.getCamera(cameraIds[ID])
    camera0 = vimba.getCamera(cameraId)
    camera0.openCamera()
      
    # list camera features
    cameraFeatureNames = camera0.getFeatureNames()
    for name in cameraFeatureNames:
        print(name)
    
    # get the value of a feature
    print(camera0.AcquisitionMode)
    
    # set the value of a feature
    camera0.AcquisitionMode = 'SingleFrame'
    
    # create new frames for the camera
    frame0 = camera0.getFrame()    # creates a frame
    frame1 = camera0.getFrame()    # creates a second frame
    
    # announce frame
    frame0.announceFrame()
    
    # capture a camera image
    camera0.startCapture()
    frame0.queueFrameCapture()
    camera0.runFeatureCommand('AcquisitionStart')
    camera0.runFeatureCommand('AcquisitionStop')
    frame0.waitFrameCapture()
    
    # get image data...
    imgData = frame0.getBufferByteData()
    
    # ...or use NumPy for fast image display (for use with OpenCV, etc)
    import numpy as np
    moreUsefulImgData = np.ndarray(buffer = frame0.getBufferByteData(),
                                   dtype = np.uint8,
                                   shape = (frame0.height,
                                            frame0.width,
                                            1))
    
    import cv2
    cv2.imshow('image', moreUsefulImgData)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # clean up after capture
    camera0.endCapture()
    camera0.revokeAllFrames()