import numpy as np
from keras.datasets import mnist
(train_X, train_Y), (test_X, test_Y) = mnist.load_data()

matrices = dict()
nums = set(train_Y)
for item in nums:
	matrices[item] = np.zeros((28, 28), dtype=float)

for i in range(len(train_Y)):
	matrices[train_Y[i]] += train_X[i]
