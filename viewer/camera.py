from __future__ import absolute_import, print_function, division
from pymba import *
import numpy as np
import cv2
import time
import sys

def frame_iterator(camera_index):
  with Vimba() as vimba:
    system = vimba.getSystem()

    system.runFeatureCommand("GeVDiscoveryAllOnce")
    time.sleep(0.2)

    camera_ids = vimba.getCameraIds()

    for cam_id in camera_ids:
        print("Camera found: ", cam_id)

    c0 = vimba.getCamera(camera_ids[camera_index])
    c0.openCamera()

    try:
        #gigE camera
        print("Packet size:", c0.GevSCPSPacketSize)
        c0.StreamBytesPerSecond = 100000000
        print("BPS:", c0.StreamBytesPerSecond)
    except:
        #not a gigE camera
        pass

    #set pixel format
    c0.PixelFormat = "BGR8Packed"  # OPENCV DEFAULT
    time.sleep(0.2)

    frame = c0.getFrame()
    frame.announceFrame()

    c0.startCapture()

    framecount = 0
    droppedframes = []

    while 1:
        try:
            frame.queueFrameCapture()
            success = True
        except:
            droppedframes.append(framecount)
            success = False

        c0.runFeatureCommand("AcquisitionStart")
        c0.runFeatureCommand("AcquisitionStop")
        frame.waitFrameCapture(1000)
        frame_data = frame.getBufferByteData()
        if success:
          img = np.ndarray(buffer=frame_data,
                             dtype=np.uint8,
                             shape=(frame.height, frame.width, frame.pixel_bytes))
          framecount += 1
          yield img

    c0.endCapture()
    c0.revokeAllFrames()

    c0.closeCamera()
    
if __name__ == '__main__':
  c0 = camera(0)
  for i in range(20):
    img = next(c0)
    print(img.shape)