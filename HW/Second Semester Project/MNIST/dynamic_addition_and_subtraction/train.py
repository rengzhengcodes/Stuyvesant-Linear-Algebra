import numpy as np
import json
from keras.datasets import mnist
(train_X, train_Y), (test_X, test_Y) = mnist.load_data()

matrices = dict()
nums = set(train_Y)
for item in nums:
	matrices[int(item)] = np.zeros((28, 28), dtype=float)

for i in range(len(train_Y)):
	max_score = 0
	best_val = None
	vector = np.reshape(train_X[i], (28 * 28))
	vector = vector / np.linalg.norm(vector)
	results = dict()

	for key, value in matrices.items():
		results[key] = value.reshape((28 * 28)).dot(vector)
		if results[key] > max_score:
			max_score = results[key]
			best_val = key

	if best_val == train_Y[i]:
		# incentivizes keeping this argument
		matrices[best_val] += train_X[i]
	else:
		# removes errors from others
		nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
		nums.remove(train_Y[i])

		for num in nums:
			matrices[num] -= train_X[i]

for key, value in matrices.items():
	matrices[key] = value / np.linalg.norm(value)

for key, value in matrices.items():
	matrices[key] = value.tolist()

print(matrices)

json.dump(matrices, open("matrices.json", "w"))
