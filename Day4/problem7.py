#Replace all negative values in an array with 0
import numpy as np

arr = np.array([10, -5, 20, -15, 30, -1])

# Option 1: In-place replacement using boolean indexing
arr[arr < 0] = 0

print("Array after replacing negatives:", arr)