#Create a 3*3 matrix using arange and reshape , then print row sums and columns sums.
import numpy as np

# Create a 3x3 matrix with values from 0 to 8
matrix = np.arange(9).reshape(3, 3)

# Calculate row sums (along axis 1) and column sums (along axis 0)
row_sums = matrix.sum(axis=1)
col_sums = matrix.sum(axis=0)

print("Matrix:")
print(matrix)

print("\nRow Sums:")
print(row_sums)

print("\nColumn Sums:")
print(col_sums)

""" OUTPUT : 
Matrix:
[[0 1 2]
 [3 4 5]
 [6 7 8]]

Row Sums:
[ 3 12 21]

Column Sums:
[ 9 12 15] """
