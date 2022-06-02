import numpy as np
import json
from keras.datasets import mnist
(train_X, train_Y), (test_X, test_Y) = mnist.load_data()

matrices = dict()
nums = set(train_Y)
for item in nums:
	matrices[int(item)] = np.zeros((28, 28), dtype=float)

for i in range(len(train_Y)):
	matrices[train_Y[i]] += train_X[i]

for key in matrices:
	nums = set(train_Y)
	nums.remove(key)

	for num in nums:
		matrices[key] -= matrices[num]

for key, value in matrices.items():
	matrices[key] = value / np.linalg.norm(value)

for key, value in matrices.items():
	matrices[key] = value.tolist()

print(matrices)

json.dump(matrices, open("matrices.json", "w"))
