## https://www.askpython.com/python/examples/load-and-plot-mnist-dataset-in-python
import numpy as np

def collapse_3D_2D(m3D:np.ndarray) -> np.ndarray:
	if m3D.ndim == 3:
		return m3D.reshape((m3D.shape[0], 28 * 28))
	else:
		raise ValueError("Expected 3D array, got " + m3D.ndim)

def regress2D_matrix(matrix:np.ndarray, result_vector:np.ndarray) -> np.ndarray:
	# q, r = np.linalg.qr(matrix) # decomposes to independent portions
	temp = matrix.transpose()@matrix
	np.savetxt("temp.csv", temp, delimiter=",")
	return np.linalg.inv(temp)@matrix.transpose()@result_vector
