import cv2
import numpy as np
import time
import os
import threading as MT
import Logger.logger as AppLogger

class ImageProcessing(object):
    
    #basic constructor for the Image Processing class taking the video stream the stream number
    # and the model as parameters
    def __init__(self,video):

        self.video=video
        self.hsv = []
        self.frame=[]

    def startStream(self):
        try:
            cap = self.video
            AppLogger.ApplicationLogger.logInfo()
            if cap.isOpened():
                ret,self.frame = cap.read()
            else: 
                ret = False
            while ret:
                
                ret,self.frame = cap.read()
                cv2.imshow('Webcam',self.frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    cap.release()
        except:
            print("Error in stream starting and processing")     
