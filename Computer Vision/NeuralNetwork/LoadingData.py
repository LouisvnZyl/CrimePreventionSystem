import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tensorflow as tf
import keras as keras
import os
import cv2
import random
import pickle
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D

#Specify the path  to your dataset
DATADIR = "D:/Honours Project/CrimePreventionSystem/Computer Vision/NeuralNetwork/Dataset"
#create your own category list 
CATEGORIES = []
#or use a loop to create them for you.
#Feel free to change this part to suit your needs
CATEGORIES = ["Gun"]
    
#Defines a fixed size of the image so that it is easy to work with     
IMG_SIZE = 100
training_data = []

#method that will create the data and use the categories to find the directories of the categories in the dataset and read them
#with that set class
def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR,category)
        Class_num = CATEGORIES.index(category)
        print(path)
        print('Processing Images...')
        for img in os.listdir(path):
            try:
                #Reads each image and converts them to RGB as cv2 is in the BGR format when you read an image
                img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, Class_num])
            except Exception as e:
                pass
        print('Done Processing')

#Calls the data reading method and saves it in a global array training_data
create_training_data()
print(len(training_data))

#Shuffles the data so that the classes wont followq in chronological order so that it improves the efficiance and accuracy of the model.

random.shuffle(training_data)

#x is your feature set 
X=[]
#y is your lables
y=[]

#adds the images with their lables in x and y arrays respectively within the training data
for features, label in training_data:
    X.append(features)
    y.append(label)

#Converst arrays to numpy arrays as the deep learning model works with these arrays.
#Reshape the image array to a set size and use the last variable to declare the size of the array within the array (Jagged array)
#as RGB will contain 3 values in that array and thus it is equal to 3
X = np.array(X).reshape(-1,IMG_SIZE,IMG_SIZE,1)
y=np.array(y)

#Pickles (saves) the data in the directory specified.
pickle_out = open("StoredSet/X.pickleRGB","wb")
pickle.dump(X,pickle_out)
pickle_out.close()

pickle_out = open("StoredSet/y.pickleRGB","wb")
pickle.dump(y,pickle_out)
pickle_out.close()
print('Data Loaded and Stored')
