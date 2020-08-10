import cv2
import tensorflow as tf
#These categories will be decided through the dataset.
categories = ["blue","green","red"]

class ObjectDetection(object):
    

    def __init__(self,frame,model):
        self.frame = frame
        self.model=model

    #Prepares the frame so thet the prediction can be done by comparing it to the model with a set frame/image size
    def prepare_img(self):
        try:
            IMG_SIZE = 100
            img_arr = cv2.imread(self.frame,cv2.IMREAD_GRAYSCALE)
            print(img_arr)
            img_arr = img_arr/255
            new_arr = cv2.resize(img_arr,(IMG_SIZE,IMG_SIZE))
            print("Image Prepared")
        except:
            print("Error in image Preparation")
        return new_arr.reshape(-1,IMG_SIZE,IMG_SIZE,1)

    #Tests the frame and gives a prediction of the object in the frame
    def TestFrame(self):   
        try:
            prep = Prepare(self.frame)    
            prediction = self.model.predict([prep.prepare_img()])    
            return categories[int(prediction[0][0])]
        except: 
            return("Error in Calculation")
        

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
            print("Error in image Preparation")
        return new_arr.reshape(-1,IMG_SIZE,IMG_SIZE,3)

model = tf.keras.models.load_model("Model_Testing/128x3-cnn.model")
print("Model Loaded")
obj = ObjectDetection("Model_Testing/Red.jpg",model)

print("Result: " + obj.TestFrame())