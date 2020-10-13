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
        
        self.model.add(Conv2D(64,(3,3),input_shape=self.X.shape[1:]))
        self.model.add(Activation("relu"))
        self.model.add(MaxPooling2D(pool_size=(2,2)))

        self.model.add(Conv2D(64,(3,3)))
        self.model.add(Activation("relu"))
        self.model.add(MaxPooling2D(pool_size=(3,3)))

        self.model.add(Conv2D(32,(3,3)))
        self.model.add(Activation("relu"))
        self.model.add(MaxPooling2D(pool_size=(5,5)))

        self.model.add(Dropout(0.25))

        self.model.add(Flatten())
        self.model.add(Dense(64))
        self.model.add(Activation("softmax"))
     
        self.model.compile(loss="sparse_categorical_crossentropy",optimizer="adam",metrics=['accuracy'])
     
        self.model.fit(self.X,self.y,batch_size=50,epochs=4,validation_split=0.1)
        self.model.save("BaseVGGNET-4-Epochs-cnn.model")

modelRun = ReluDropoutRGB(X,y,newMod)
#Runs the model method to train and save the model from the dataset
modelRun.Model()