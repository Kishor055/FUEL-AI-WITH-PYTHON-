#Create a 4*4 Identity matrix and multiply it by 5.
import numpy as np

# Create a 4x4 Identity matrix
identity_matrix = np.eye(4)

# Multiply by 5
#np.eye is a NumPy function that returns a 2D array with ones on the diagonal and zeros elsewhere
result = identity_matrix * 5

print("Identity Matrix (4x4):")
print(identity_matrix)

print("\nAfter multiplying by 5:")
print(result)