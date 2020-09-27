import cv2
from Image_Processsing import ImageProcessing
import threading as MT
from Logger import logger
try:
    #Loads in the saved model.
    #model = tf.keras.models.load_model("Main/128x3-cnn.model")
    #Creates the diffirent video stream. In this case we duplicated the first one to simulate 3 cameras.
    # Video 1 and 2 will be the frontal cameras and video 3 the bottom one.
    print('Starting Application')
    video1 = cv2.VideoCapture(0)

    #Creating Process instances of the image procassing class parsing the stream the video number and the model.
    imageProcess = ImageProcessing(video1)

    #Creation of the threads for each stream with the target being the start sream method in the video processing class.
    print("Creating Threads")
    
    t1 = MT.Thread(target=imageProcess.startStream)
    t1.start()

    #Joinging of the threads when they are finished executing so that they can safely close.
    t1.join()

    print("Application Terminated")
    #closing all open windows
    cv2.destroyAllWindows()
    #releasing the video input devices and turing them off.
    video1.release()
except:
    print("Failed to run or close the application properly")

    

