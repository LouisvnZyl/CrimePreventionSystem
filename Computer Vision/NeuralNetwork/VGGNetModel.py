#Importing all of the needed libraries and giving it a name that we will use
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import keras as keras
import pickle
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import TensorBoard
#Uses a secuential model
newMod = Sequential()
#Loads in the saved data 
X= pickle.load(open("D:\Honours Project\CrimePreventionSystem\Computer Vision\StoredSet\X.pickle","rb"))
y=pickle.load(open("D:\Honours Project\CrimePreventionSystem\Computer Vision\StoredSet\y.pickle","rb"))

class ReluDropoutRGB(object):
#Creation of the constreuctor to gather the variables needed
#X being the stored images, y the lables then your convolutional layer size, the layer size and the amount of dense layers you need.
    def __init__(self, X,y,model):
        self.X=X
        self.y=y
        self.model=model
        
#Defining the model method th use the variables in set object to perform the defined model
    def Model(self):
        self.model = Sequential()
        
#Uses set variables to create the loop for executinmg diffirent varibales in a array on the set model.
        
        #Name for the saving of the trained model to view it with Tensorboard
        #Defining a 2d convolutional layer on the given image array and using the relu activation function and will pool a 2x2 array and find the largest number
        self.model.add(Conv2D(5,(3,3),input_shape=self.X.shape[1:]))
        self.model.add(Activation("relu"))
        self.model.add(MaxPooling2D(pool_size=(2,2)))
        self.model.add(Flatten())
        self.model.add(Activation("softmax"))
        #Creates more convolutional layers depending on the given variable and uses the relu activation function       
        self.model.compile(loss="sparse_categorical_crossentropy",optimizer="adam",metrics=['accuracy'])
        #Now we will fit the model using the images found in x and categorizing it in y using 32 images at a time, having 10 iterations.
        #It will use 10% of the data to validate the trained model and use the tensorboard callback.
        self.model.fit(self.X,self.y,batch_size=25,epochs=3,validation_split=0.1)
        self.model.save("BaseVGGNET")
    #def useModel(self):
#creates an instance of the model class with the images, classes and the model base as parameters
modelRun = ReluDropoutRGB(X,y,newMod)
#Runs the model method to train and save the model from the dataset
modelRun.Model()