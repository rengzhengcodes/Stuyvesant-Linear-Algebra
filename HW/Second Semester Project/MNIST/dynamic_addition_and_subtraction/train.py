import numpy as np
import json
from keras.datasets import mnist
(train_X, train_Y), (test_X, test_Y) = mnist.load_data()

# aggregated all data
temp = json.load(open("start.json"))
matrices = dict()

for key, value in temp.items():
	matrices[int(key)] = value

del temp
print(matrices)
for i in range(1):
	for i in range(len(train_Y)):
		max_score = 0
		best_val = 0
		vector = np.reshape(train_X[i], (28 * 28))
		vector = vector / np.linalg.norm(vector)
		results = dict()

		for key, value in matrices.items():
			results[key] = np.reshape(value, (28 * 28)).dot(vector)
			if results[key] > max_score:
				max_score = results[key]
				best_val = key

		if best_val == train_Y[i]:
			# incentivizes keeping this argument
			matrices[best_val] += train_X[i]
		else:
			# removes errors from that guess
			matrices[best_val] -= train_X[i]

for key, value in matrices.items():
	matrices[key] = value / np.linalg.norm(value)

for key, value in matrices.items():
	matrices[key] = value.tolist()

print(matrices)

json.dump(matrices, open("matrices.json", "w"))
