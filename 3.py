"""
For this code we need to import two famous third party
library into our code. numpy, opencv.

Numpy: for working with arrays (efficiently and fast)
Opencv: Open Source Computer Vision Library

the goal of this code is to use opencv to do
OCR (Optical character reader) for numbers.

after installing opencv and numpy
using pip, you can go to:
http://opencv.org/opencv-3-2.html

and download the source. it contains so many
useful packages and data for face recognition
and object tracking and so on...also there's an
image called "digits.png" which we need here.
"""
import numpy as np
import cv2


img = cv2.imread('numbers.png') # this is how you read an image.
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # turning it into gray (one channle instead of three RGB)
cv2.imshow("test",gray)
cv2.waitKey(0)
# Now we split the image to 5000 cells, each 20x20 size with a number in each cell:
# cells = [np.hsplit(row,1) for row in np.vsplit(gray,3)]
cells = np.split(gray,3)
# Make it into a Numpy array. It size will be (50,100,20,20):
x = np.array(cells)
# Now we prepare train_data and test_data.
train = x[:,:].reshape(-1,400).astype(np.float32) # Size = (2500,400)
# Create labels for train and test data
k = np.arange(10)
train_labels = np.repeat(k,500)[:,np.newaxis]
test_labels = train_labels.copy()
# Initiate kNN, train the data, then test it with test data for k=1
knn = cv2.ml.KNearest_create() # KNearest is a classification algorithem. look at the end of code.
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels) # training our machine to learn the trend of data.
# ok...now we have done the training part.
# let's try to see if it can actually read numbers:

'''
1) open paint and draw a number in a 20*20 pixel canvas.
2) Invert it's color so the box be black and your
 number be in white.
3) save as something.png and close it.
'''
number_iamge = cv2.imread('something.png')
gray = cv2.cvtColor(number_iamge,cv2.COLOR_BGR2GRAY)
x = np.array(gray).reshape(-1,400).astype(np.float32)
ret,result,neighbours,dist = knn.findNearest(x,k=1)
print(result)

# for more info on k-Nearest Neighbour:
# http://docs.opencv.org/trunk/d5/d26/tutorial_py_knn_understanding.html
# for more info on Machine Learning:
# http://docs.opencv.org/trunk/d6/de2/tutorial_py_table_of_contents_ml.html
# also:
# http://www.nptel.ac.in/courses/106108057/1#
# this code is modification of this source code:
# http://docs.opencv.org/trunk/d8/d4b/tutorial_py_knn_opencv.html

# tip: you can open the training image that i mention in line 24 with paint
# and invert its color therefore you don't have to invert the
# color of numbers you write in paint afterwards in something.png!
'''it goes without saying: this code doesn't work on sololearn'''
