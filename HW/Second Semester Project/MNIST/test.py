import lin_reg

def collapse_3D_2D_manual(m3D:np.ndarray) -> np.ndarray:
	if m3D.ndim == 3:
		arr = list()
		m3D = m3D.tolist()

		for row in n3D:
			row = list()
			for column in row:
				for height in column:
					row.append(height)
			arr.append(list)

		return np.asarray(arr)
	else:
		raise ValueError("Expected 3D array, got " + m3D.dim)

# loads data from tuples
from keras.datasets import mnist
(train_X, train_Y), (test_X, test_Y) = mnist.load_data()
train_X_lin = lin_reg.collapse_3D_2D(train_X)
train_X_man = collapse_3D_2D_manual(train_X)

print("3D to 2D: " + train_X_lin == train_X_man)
