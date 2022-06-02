import numpy as np
import json
from keras.datasets import mnist
import matplotlib.pyplot as plt
(train_X, train_Y), (test_X, test_Y) = mnist.load_data()

matrices = json.load(open("matrices.json"))

"""
for key, value in matrices.items():
	plt.matshow(value)

plt.show()
"""


for key, value in matrices.items():
	# print(value)
	matrices[key] = np.array(value)
	# print(matrices[key])
	matrices[key] = np.reshape(matrices[key], (28*28))
	# print(matrices[key])

correct = 0
incorrect = 0

for i in range(len(test_Y)):
	results = dict()
	max_score = 0
	best_val = None
	vector = np.reshape(test_X[i], (28 * 28))
	vector = vector / np.linalg.norm(vector)

	for key, value in matrices.items():
		results[key] = value.dot(vector)
		if results[key] > max_score:
			max_score = results[key]
			best_val = key

	if int(best_val) == test_Y[i]:
		correct += 1
	else:
		print(i)
		print(results)
		incorrect += 1

print(correct, incorrect)
