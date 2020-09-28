import cv2
import tensorflow as tf
#These categories will be decided through the dataset.

categories = ["Gun","Hand"]

class ObjectDetection(object):
    
    def __init__(self,frame,model):
        self.frame = frame
        self.model = model

    #Tests the frame and gives a prediction of the object in the frame
    def TestFrame(self):
        try:
            prep = Prepare(self.frame)    
            prediction = self.model.predict([prep.prepare_img()])
            return categories[int(prediction[0][0])]
        except:
            return("Error in prediction !")
        
        
class Prepare(object):
    def __init__(self,frame):
        self.frame = frame

    def prepare_img(self):
        try:
            IMG_SIZE = 500
            new_arr = cv2.resize(self.frame,(IMG_SIZE,IMG_SIZE))
            return new_arr.reshape(-1, IMG_SIZE,IMG_SIZE, 1)
        except:
            print('Error in image preparation')