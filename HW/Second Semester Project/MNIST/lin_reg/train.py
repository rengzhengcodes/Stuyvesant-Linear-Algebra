import lin_reg
from keras.datasets import mnist
(train_X, train_Y), (test_X, test_Y) = mnist.load_data()

result = lin_reg.regress2D_matrix(lin_reg.collapse_3D_2D(train_X), train_Y.transpose())
result.savetxt("res.csv", result, delimiter=',')
