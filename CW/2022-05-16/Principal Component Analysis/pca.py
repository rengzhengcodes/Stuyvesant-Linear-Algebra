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

def pca(data:np.array):
	"""
	Conducts principle component analysis
	"""
	data = demean(data)
	# forms covariant matrix
	covariant_matrix = data.transpose()@data
	covariant_matrix = covariant_matrix/len(data)

	# finds eigenvectors and eigenvalues
	raw_results = np.linalg.eig(covariant_matrix)

	# converts to dict
	results = dict()

	for i in range(len(raw_results[0])):
		results[raw_results[0][i]] = raw_results[1][i]

	return results

print(pca(data))
