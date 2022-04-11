### Frobenius inner product computation
import numpy as np

def frobenius(matrix1, matrix2):
	matrix1 = matrix1.transpose()
	multiplied = np.matmul(matrix1, matrix2)

	if multiplied.ndim <= 1:
		return int(multiplied)
	else:
		return multiplied.trace()

### Tests
matrix1 = np.array([1, 1, 1, 1, 1]) # Dot product
print(frobenius(matrix1, matrix1), np.inner(matrix1, matrix1))
matrix2 = np.array([0, 0, 0, 0, 0])
print(frobenius(matrix1, matrix2), np.inner(matrix1, matrix2))
matrix3 = np.array([[1, 2, 3, 4, 5],
					[1, 2, 3, 4, 5]])
matrix4 = np.array([[1, 1, 1, 1, 1],
					[1, 1, 1, 1, 1]])
print(frobenius(matrix3, matrix4), np.inner(matrix3, matrix4).trace())
matrix4 = np.array([[8663, 1, 1, 124, 1],
					[1, 132, 1, 1324, 1]])
print(frobenius(matrix3, matrix4), np.inner(matrix3, matrix4).trace())
