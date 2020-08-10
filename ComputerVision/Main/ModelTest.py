import cv2
#import tensorflow as tf
#These categories will be decided through the dataset.

pickle_out = open("y.pickle","wb")

class ObjectDetection(object):
    categories = ["blue","green","red"]

    def __init__(self,frame,model):
        self.frame = frame
        self.model=model

    #Tests the frame and gives a prediction of the object in the frame
    def TestFrame(self):
        try:
            prep = Prepare(self.frame)    
            prediction = self.model.predict([prep.prepare_img()])
            return str(categories[int(prediction[0][0])])
        except:
            return("Error in prediction !")
        
        
class Prepare(object):
    def __init__(self,frame):
        self.frame = frame

    def prepare_img(self):
        try:
            IMG_SIZE = 100
            img_arr = cv2.imread(self.frame,cv2.COLOR_BGR2RGB)
            print(img_arr)
            img_arr = img_arr/255
            new_arr = cv2.resize(img_arr,(IMG_SIZE,IMG_SIZE))
            print("Image Prepared")
        except:
            print("Error in prediction")
        return new_arr.reshape(-1,IMG_SIZE,IMG_SIZE,3)