import numpy as np

listA = [
	[2, -1, 0],
	[3, -4, 1],
	[4, 3, 0]
]

print("A as a list of lists \n", listA, "\n")

# converts list to array
A1 = np.asarray(listA)
print("A as a numpy array with integer entries \n", A1, "\n")

A2 = np.asarray(listA, dtype=float)
print("A as a numpy array with float entries \n", A2, "\n")

#creating numpy arrays
#creating 1D arrays in numpy
#Numpy's arrange creates consecutive sequences
B1 = np.arange(3, 11, dtype=float)
print("np.arange creates a 1D consecutive sequence: \n", B1, "\n")

#Numpy's linspace creates arithmetic sequences
B2 = np.linspace(4., .25, 16)
print("np.linspace creates a 1D arithmetic progression: \n", B2, "\n")

#Numpy has built-in identity matrix functions
I1 = np.eye(4)
I2 = np.eye(4, 6)

print("A 4x4 identity matrix: \n", I1, "\n")
print("A 4x4 identity matrix with two additional columns of 0s: \n", I2, "\n")

#Numpy has built-in diagonal matrix functions
D1 = np.diag([-4, 3, 0, 1])
D2 = np.diag([2, -1, 3], 2)

print("A diagonal matrix with given entries: \n", D1, "\n")
print("A diagonal matrix with given entries and two leading columns of 0s: \n", D2, "\n")

# The function diag can also return the diagonal entries of an existing matrix
print("The diagonal elements of the matrix \n", A2, "\n are \n", np.diag(A2), "\n")

# built-in all 0s and 1s matrices
# Notice: the parameter here is a tuple (m, n)

All1s = np.ones((3, 2))
All0s = np.zeros((2, 5))

print("A 3x2 all 1s matrix: \n", All1s, "\n")
print("A 2x5 0 matrix: \n", All0s, "\n")

#Simple generation of random multi-dimensional arrays
#Notice np.random.random takes dimensions as a tuple

R1 = np.random.random((3, 3))

print("A random 3x3 matrix: \n", R1, "\n")

R2 = np.random.uniform(-1, 1, (3, 3))

print("A random 3x3 matrix with uniform entries between -1 and 1: \n", R2, "\n")

#Randint returns random integers. NOTE the parameter is upper bound + 1
R3 = np.random.randint(2, size = (4, 4))
R4 = np.random.randint(-10, 10, size = (3, 3))

print("A random 4x4 matrix with all entries 0 or 1: \n", R3, "\n")
print("A random 3x3 matrix with all entries between -10 and 9: \n", R4, "\n")
