The main application can be found in the main folder.

In this folder the MianRun.py file is used to execute the application.
Note you will have to have Opencv2 installed as well as Tensorflow_GPU or CPU but GPU is preferred.

The model_testing file contains the model as well as the Loading data method wich will read the data
from the directory specified and create pickle files which the data is stored in thus there is no need to 
load them each time.

The image_model_test file is just used to test a static image against the model to see what 
classification it gives you but the model and testing still needs work.

The Neaural network class contains the physical model and it is trained using the datasets
that you provide and saves the model with a name you want and that is clear on what
the model consists of.

Feel free to contact me if there is any assistance needed. I will gladly help.
Just note that there are still some features that I am working on and that
the screen may seem bloated with all of the text when it detects a contour colour.
This only happens if it sees many diffirent "shapes". If it detects only one
then only one text instance and mid pint will be show. If this occurs where there
are multiple locations that it sees as diffirent objects the performance of the stream
will become poor but not tho an unuseable extent.