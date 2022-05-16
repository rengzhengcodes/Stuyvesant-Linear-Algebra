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

print(data)
