import time
import cv2
import numpy as np
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)

class LineFollow(object):

    def __init__(self,frame):
        self.frame=frame
    
    def VisualizeLine(self):
        try:
            #cv2.imshow('Pre-Process',frame)
            # Crop the image
    
            # Convert to grayscale
            gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            # Gaussian blur
            blur = cv2.GaussianBlur(gray,(5,5),0)
            # Color thresholding
            ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)
            # Find the contours of the frame
            _,contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)
            # Find the biggest contour (if detected)
    
            if len(contours) > 0:

                c = max(contours, key=cv2.contourArea)
                M = cv2.moments(c)
                cx = int(M['m10']/M['m00'])

                cy = int(M['m01']/M['m00'])

                cv2.line(self.frame,(cx,0),(cx,720),(255,0,0),1)
                cv2.line(self.frame,(0,cy),(1280,cy),(255,0,0),1)
                cv2.drawContours(self.frame, contours, -1, (0,255,0), 1)

                if cx >= 740:

                    #print("Turn Left!")
                    GPIO.output(8, GPIO.HIGH)
                    GPIO.output(25, GPIO.HIGH)
                    if cx >=840:
                        GPIO.output(25, GPIO.LOW)
                        GPIO.output(24, GPIO.LOW)
                    
                elif cx < 840 and cx > 440:
                    
                    #print("On Track!")
                    GPIO.output(25, GPIO.HIGH)
                    GPIO.output(8, GPIO.LOW)
                    GPIO.output(24, GPIO.LOW)
                elif cx <= 540:
         
                    #print("Turn Right")
                    GPIO.output(24, GPIO.HIGH)
                    GPIO.output(25, GPIO.HIGH)
                    if cx <= 440:
                        GPIO.output(8, GPIO.LOW)
                        GPIO.output(25, GPIO.LOW)

                else:
                    print("I don't see the line")
                    
        except:
            print("Error in calculating the line")
            GPIO.output(15, GPIO.LOW)

        return self.frame
