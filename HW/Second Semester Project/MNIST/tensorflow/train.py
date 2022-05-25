# Source: https://www.kaggle.com/code/urmishah/mnist-dataset-linear-regression-dl/notebook

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.datasets.mnist import load_data
(x_train, y_train), (x_test, y_test) = load_data()

"""
# Looking at the data

print(x_train.shape)
print(x_test.shape)

# shape of data
print(x_train[0])
#image
plt.matshow(x_train[0])
plt.show()
#confirm
print(y_train[0])
# normalize the data
"""

"""
Data Preprocessing
"""

# data normalization
x_train = x_train / 255
x_test = x_test / 255
# divding by 255 to make the pixel values from 0-1 instead of 0-255

"""
# check
print(x_train[0])
"""

# flaten the 2d data to 2 dims
# The data is 3D because its 60000 units of a 28x28 grid

# converts the 2d image to 1d
x_train_flattened = x_train.reshape(len(x_train), 28 * 28)
x_test_flattened = x_test.reshape(len(x_test), 28 * 28)

print(x_train_flattened.shape)

# Defining the model
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from numpy.random import seed
import tensorflow

model = Sequential()
model.add(Dense(10, input_shape=(784,), activation='sigmoid'))

model.summary()

# compiling the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Fitting the model
model.fit(x_train_flattened, y_train, epochs=10)

# Evaluating the model
model.evaluate(x_test_flattened, y_test)

# make prediction
y_predicted = model.predict(x_test_flattened)

# probabilities per number
print(y_predicted[0])

# find a maximum element from an array and returns its index (here it corresponds to the number predicted)
print(np.argmax(y_predicted[0]))

#check
plt.matshow(x_test[0])
plt.show()
