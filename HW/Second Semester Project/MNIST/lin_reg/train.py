import lin_reg
import numpy as np
from keras.datasets import mnist
(train_X, train_Y), (test_X, test_Y) = mnist.load_data()

train_X = train_X / 255

result = lin_reg.regress2D_matrix(lin_reg.collapse_3D_2D(train_X), train_Y.transpose())
norm = np.linalg.norm(result)
result = result / norm
np.savetxt("res.csv", result, delimiter=',')
