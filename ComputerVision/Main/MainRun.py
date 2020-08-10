from Image_Processsing import ImageProcessing
import cv2
import threading as MT
import time


#import tensorflow as tf
try:
    #Loads in the saved model.
    #model = tf.keras.models.load_model("Main/128x3-cnn.model")
    #Creates the diffirent video stream. In this case we duplicated the first one to simulate 3 cameras.
    # Video 1 and 2 will be the frontal cameras and video 3 the bottom one.
    video1 = cv2.VideoCapture(0)
    #setting the width and the height of the stream.
    video1.set(3,1280)
    video1.set(4,720)

    video2 = video1
    video3 = video2

    #Creating Process instances of the image procassing class parsing the stream the video number and the model.
    process1 = ImageProcessing(video1,1)
    process2 = ImageProcessing(video2,2)
    process3 = ImageProcessing(video3,3)

    #Creation of the threads for each stream with the target being the start sream method in the video processing class.
    print("Creating Threads")
    t1 = MT.Thread(target=process1.startStream)
    t1.start()
    time.sleep(10)
    t2 = MT.Thread(target=process2.startStream)
    t2.start()
    time.sleep(10)
    t3 = MT.Thread(target=process3.startStream)
    t3.start()

    #Joinging of the threads when they are finished executing so that they can safely close.
    t1.join()

    t2.join()

    t3.join()


    print("Application Terminated")
    #closing all open windows
    cv2.destroyAllWindows()
    #releasing the video input devices and turing them off.
    video1.release()
except:
    print("Failed to run or close the application properly")

    

