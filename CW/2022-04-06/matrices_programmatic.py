import numpy as np

#Initialize a 2D list by creating a list of lists of 0s
MList = [[0]*4 for i in range(3)]

#Here's the initialized Python list of lists
print("Initialized list of lists: \n", MList, "\n")

#Now changes the entries programatically
#In this example, each entry is the sum of its indices
#Notice the first FOR iterates over the list of lists, the second FOR iterates over each individual list
for i in range(len(MList)):
	for j in range(len(MList[i])):
		MList[i][j] = i + j

#Print the updated list of lists
print("Updated list of lists: \n", MList, "\n")

#Convert the list of lists to a Numpy array and print
M = np.asarray(MList)
print("The matrix M: \n", M, "\n")

#Examples of slicing numpy arrays
#Notice how all slices are returned as "rows" (that is, as 1D arrays)

print("The first row of M is:", M[0], "\n")
print("The third row of M is:", M[2], "\n")
print("The first column of M is:", M[0,0:3], "\n")
print("The third column of M is:", M[2,0:3], "\n")
