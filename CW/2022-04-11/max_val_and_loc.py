### Maximum value and location


import numpy as np

def max_value(matrix):
	return np.amax(matrix)

def max_loc(matrix):
	result = np.where(matrix == max_value(matrix))
	return result

def max_value_and_location(matrix):
	return (max_value(matrix), max_loc(matrix))

# tests
matrix = np.array([1])
print(max_value_and_location(matrix))

matrix = np.array([[1, 1, 1, 1, 1, 1, 1, 2],
		   [1, 2, 34,3, 2, 1, 1, 0]])

print(max_value_and_location(matrix))
