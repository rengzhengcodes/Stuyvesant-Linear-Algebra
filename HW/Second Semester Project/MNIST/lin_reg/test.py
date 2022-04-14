import lin_reg
import numpy as np

def collapse_3D_2D_manual(m3D:np.ndarray) -> np.ndarray:
	if m3D.ndim == 3:
		arr = list()
		m3D = m3D.tolist()

		for row in m3D:
			row_new = list()
			for column in row:
				for height in column:
					row_new.append(height)
			arr.append(row_new)

		return np.asarray(arr)
	else:
		raise ValueError("Expected 3D array, got " + m3D.dim)

# loads data from tuples
from keras.datasets import mnist
(train_X, train_Y), (test_X, test_Y) = mnist.load_data()
train_X_lin = lin_reg.collapse_3D_2D(train_X)
## np.savetxt("foo.csv", train_X_lin, delimiter=",")
print(train_X_lin)
(train_X, train_Y), (test_X, test_Y) = mnist.load_data()
train_X_man = collapse_3D_2D_manual(train_X)
print(train_X_man)
## np.savetxt("bar.csv", train_X_man, delimiter=",")

print("3D to 2D: " + str(np.array_equal(train_X_lin, train_X_man)))
