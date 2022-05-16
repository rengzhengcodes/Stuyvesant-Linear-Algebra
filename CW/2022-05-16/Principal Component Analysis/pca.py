"""
imports data
"""
import csv

file = csv.reader(open("2D_data.txt"))
data = list(file)
# str to integers
data = [[float(x), float(y)] for x, y in data]

"""
converts to matrix
"""
import numpy as np

data = np.array(data)

"""
analyzes data
"""
def demean(data:np.array):
	"""
	demeans array input
	"""
	# gets the mean along the columns
	means = data.mean(0)

	# subtracts means from each row
	for row in data:
		for i in range(len(means)):
			row[i] -= means[i]

	return data

