import numpy as np
from keras.datasets import mnist
(train_X, train_Y), (test_X, test_Y) = mnist.load_data()

r = np.genfromtxt("res.csv", delimiter=',')

correct = 0
incorrect = 0

for i in range(len(test_X)):
	# gets testing sample
	analyte = test_X[i]
	# takes data and shifts it into a unit vector
	sum = analyte.sum()
	analyte = analyte / sum
	analyte = analyte.reshape((1 , 28*28))
	# gets a result from projection onto subspace
	result = analyte@r
	result = float(result)
	# rounds and turns data into this
	result = round(result)
	result = abs(result)

	if result >= 10:
		print(i)
		incorrect += 1
	elif result == test_Y[i]:
		correct += 1
	else:
		incorrect += 1

print(correct, incorrect)
