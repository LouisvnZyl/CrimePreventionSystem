import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tensorflow as tf
import tensorflow.keras as keras
import os
import cv2
import random
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import time

DATADIR = "Datasets/Training_Data"
CATEGORIES = []

for i in range(42):
    if i < 10:
        CATEGORIES.append("0000" + str(i))
    else:
        CATEGORIES.append("000"+str(i))
    
     
IMG_SIZE = 50
training_data = []

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR,category)
        class_num = CATEGORIES.index(category)
        print(path)
        #time.sleep(5)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img),cv2.COLOR_BGR2RGB)
                new_array = cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
                training_data.append([new_array,class_num])
            except Exception as e:
                pass

create_training_data()
print(len(training_data))

random.shuffle(training_data)

X=[]
y=[]

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1,IMG_SIZE,IMG_SIZE,1)
y=np.array(y)
pickle_out = open("X.pickleRGB","wb")
pickle.dump(X,pickle_out)
pickle_out.close()

pickle_out = open("y.pickleRGB","wb")
pickle.dump(y,pickle_out)
pickle_out.close()