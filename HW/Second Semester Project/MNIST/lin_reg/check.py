import numpy as np
from keras.datasets import mnist
(train_X, train_Y), (test_X, test_Y) = mnist.load_data()

r = np.genfromtxt("res.csv", delimiter=',')

correct = 0
incorrect = 0

for i in range(len(train_X)):
	# gets testing sample
	analyte = train_X[i]
	# takes data and shifts it into a unit vector
	norm = np.linalg.norm(analyte)
	analyte = analyte / norm
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
		print(result, train_Y[i])
	elif result == train_Y[i]:
		correct += 1
	else:
		incorrect += 1
		print(result, train_Y[i])

print(correct, incorrect)
