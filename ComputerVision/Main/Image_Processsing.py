import cv2
import numpy as np
import time
import os
import threading as MT
from LineFollowFinal import LineFollow
#import tensorflow as tf
from ModelTest import ObjectDetection

import RPi.GPIO as GPIO
#greenMask = []
#blueMask = []
#redMask = []

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)


class ImageProcessing(object):
    
    #basic constructor for the Image Processing class taking the video stream the stream number
    # and the model as parameters
    def __init__(self,video,frameno):

        self.video=video
        self.hsv = []
        self.frame=[]
        self.frmaeno = frameno
    
        
    #First of 3 methods that will calculate the colour. These methods are explained in the word documentation 
    # Note the documentation is not yet fully completed
    #Also note that these methods are identical and you can add new ones if there is a new colour to be processed. OpenCV works with the BGR range !
    def computeRed(self):
        try:
            # Red Color
            Rlow = np.array([140,150,0])
            Rhigh = np.array([180,255,255])
            RImage_mask = cv2.inRange(self.hsv,Rlow,Rhigh)
            red = cv2.bitwise_and(self.frame,self.frame,mask=RImage_mask)
        
            _,Rcontours,c2 = cv2.findContours(RImage_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        
            if Rcontours:
                GPIO.output(15, GPIO.HIGH)
            else:
                GPIO.output(15, GPIO.LOW)
            cv2.drawContours(self.frame,Rcontours,-1,(0,0,255),1)
         
        
            for c in Rcontours:
                M=cv2.moments(c)

                if (int(M["m00"])) > 0:
                    cX=int(M["m10"]/M["m00"])
                    cY = int(M["m01"]/M["m00"])
                    cv2.circle(self.frame,(cX, cY),1,(255,255,255),-1)
                    #obj = ObjectDetection(self.frame,self.model)
                    #obj.TestFrame() to use the model but it still needs work
                    #Devides frame into parts to se where the object lies using the x and y values of the set frame
                    if cX < 540: 

                        if cY <260:
                            cv2.putText(self.frame,"Red: Left-Top",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)
                        elif cY > 460:
                            cv2.putText(self.frame,"Red: Left-Bottom",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)
                        else:
                            cv2.putText(self.frame,"Red: Left-Middle",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)
                    elif cX > 740:

                        if cY <260:
                            cv2.putText(self.frame,"Red: Right-Top",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)
                        elif cY > 460:
                            cv2.putText(self.frame,"Red: Right-Bottom",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)
                        else:
                            cv2.putText(self.frame,"Red: Right-Middle",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)
                    else:
                        if cY <260:
                            cv2.putText(self.frame,"Red: Middle-Top",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)
                        elif cY > 460:
                            cv2.putText(self.frame,"Red: Middle-Bottom",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)
                        else:
                            cv2.putText(self.frame,"Red: Middle",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)
                                  
            redMask = red
        except:
            print("Error in red colour computation")
                
    def computeGreen(self):
        try:
            # Green Color
            Glow = np.array([20,70,70])
            Ghigh = np.array([80,255,255])
            GImage_mask = cv2.inRange(self.hsv,Glow,Ghigh)
            green = cv2.bitwise_and(self.frame,self.frame,mask= GImage_mask)
        
            _,Gcontours,c2 = cv2.findContours(GImage_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        
            if Gcontours:
                GPIO.output(18, GPIO.HIGH)
            else:
                GPIO.output(18, GPIO.LOW)
        
            cv2.drawContours(self.frame,Gcontours,-1,(0,255,0),1)
        
        
            for c in Gcontours:
                M=cv2.moments(c)

                if (int(M["m00"])) > 0:
                    cX=int(M["m10"]/M["m00"])
                    cY = int(M["m01"]/M["m00"])
                    cv2.circle(self.frame,(cX, cY),3,(255,255,255),-1)
                    #cv2.line(self.frame,(cX,0),(cX,720),(255,0,0),1)
                    #cv2.line(self.frame,(0,cY),(1280,cY),(255,0,0),1)
                    #obj = ObjectDetection(self.frame,self.model)
                    #obj.TestFrame() to use the model but it still needs work
                    if cX < 540: 

                        if cY <260:
                            cv2.putText(self.frame,"Green: Left-Top",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)
                        elif cY > 460:
                            cv2.putText(self.frame,"Green: Left-Bottom",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)
                        else:
                            cv2.putText(self.frame,"Green: Left-Middle",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)
                    elif cX > 740:

                        if cY <260:
                            cv2.putText(self.frame,"Green: Right-Top",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)
                        elif cY > 460:
                            cv2.putText(self.frame,"Green: Right-Bottom",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)
                        else:
                            cv2.putText(self.frame,"Green: Left-Middle",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)
                    else:
                        if cY <260:
                            cv2.putText(self.frame,"Green: Middle-Top",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)
                        elif cY > 460:
                            cv2.putText(self.frame,"Green: Middle-Bottom",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)
                        else:
                            cv2.putText(self.frame,"Green: Middle",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)
                    
            greenMask = green
        except:
            print("Error in green colour computation")
        
                
    def computeBlue(self):
        try:
            # Blue Color
            Blow = np.array([100,50,50])
            Bhigh = np.array([140,255,255])
            BImage_mask = cv2.inRange(self.hsv,Blow,Bhigh)
            blue = cv2.bitwise_and(self.frame,self.frame,mask=BImage_mask)
        
            _,Bcontours,c2 = cv2.findContours(BImage_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        
            if Bcontours:
                GPIO.output(14, GPIO.HIGH)
            else:
                GPIO.output(14, GPIO.LOW)
            
            cv2.drawContours(self.frame,Bcontours,-1,(255,0,0),1)
        
            for c in Bcontours:
                M=cv2.moments(c)

                if (int(M["m00"])) > 0:
                    cX=int(M["m10"]/M["m00"])
                    cY = int(M["m01"]/M["m00"])
                    cv2.circle(self.frame,(cX, cY),3,(255,255,255),-1)

                    #cv2.line(self.frame,(cX,0),(cX,720),(255,0,0),1)
                    #cv2.line(self.frame,(0,cY),(1280,cY),(255,0,0),1)

                    #obj = ObjectDetection(self.frame,self.model)
                    #obj.TestFrame() to use the model but it still needs work
                    if cX < 540: 
                        if cY <260:
                            cv2.putText(self.frame,"Blue: Left-Top",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
                        elif cY > 460:
                            cv2.putText(self.frame,"Blue: Left-Bottom",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
                        else:
                            cv2.putText(self.frame,"Blue: Left-Middle",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
                    elif cX > 740:
                        if cY <260:
                            cv2.putText(self.frame,"Blue: Right-Top",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
                        elif cY > 460:
                            cv2.putText(self.frame,"Blue: Right-Bottom",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
                        else:
                            cv2.putText(self.frame,"Blue: Right-Middle",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
                    else:
                        if cY <260:
                            cv2.putText(self.frame,"Blue: Middle-Top",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
                        elif cY > 460:
                            cv2.putText(self.frame,"Blue: Middle-Bottom",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
                        else:
                            cv2.putText(self.frame,"Blue: Middle",(cX-20,cY-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
            blueMask=blue
        except:
            print("Error in blue colour computation")

    def startStream(self):
        try:
            cap = self.video

            if cap.isOpened():
                ret,self.frame = cap.read()
            else: 
                ret = False
            while ret:
                GPIO.output(23, GPIO.HIGH)
                
                #print("Started the video stream")
                ret,self.frame = cap.read()
                newFrame = self.frame
                self.hsv=cv2.cvtColor(self.frame,cv2.COLOR_BGR2HSV)
                
                if self.frmaeno == 3:
                    #Sees what stream is used for the line detection to follow
                    lf = LineFollow(self.frame) 
                    self.frame = lf.VisualizeLine()
                    self.measure_temp()

                else:
                    #Starts the methods to process the diffirent colours
                    self.computeBlue()
                    self.computeGreen()
                    self.computeRed()
                    
                #Shows the video stream after countours have been drawn and its location calculated.
                #This is not needed in the end product but it is used to vusually see what the program does behind the scenes.
                #cv2.imshow("Camera {}".format(self.frmaeno),self.frame)
                    
                #cv2.imshow("Camera {}".format(self.frmaeno),newFrame)
                
                #cv2.imshow("Green Image Mask",greenMask)
                #cv2.imshow("Blue Image Mask",blueMask)
                #cv2.imshow("Red Image Mask",redMask)

                #Pressing of the ESC key will close the application
                if cv2.waitKey(1)==27:
                    GPIO.output(18, GPIO.LOW)
                    GPIO.output(14, GPIO.LOW)
                    GPIO.output(15, GPIO.LOW)
                    GPIO.output(23, GPIO.LOW)
                    GPIO.output(24, GPIO.LOW)
                    GPIO.output(25, GPIO.LOW)
                    GPIO.output(8, GPIO.LOW)
                    
                    break
            cv2.destroyAllWindows()
            cap.release()
        except:
            print("Error in stream starting and processing")     


    def measure_temp(self):
        temp= os.popen("vcgencmd measure_temp").readline()
        print(temp)
        #print(temp.replace("temp = ",""))
        



