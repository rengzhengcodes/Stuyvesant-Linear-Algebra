"""
imports data
"""
import csv

file = csv.reader(open("2D_data.txt"))
file = list(file)
# str to integers
file = [[float(x), float(y)] for x, y in file]

"""
converts to matrix
"""
import numpy as np
