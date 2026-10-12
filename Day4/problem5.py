#Normalise an array using (x-min) / (max-min)
import numpy as np

# Sample array
arr = np.array([10, 20, 30, 40, 50])

# Perform Min-Max Normalization: (x - min) / (max - min)
normalized_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

print("Original Array:", arr)
print("Normalized Array:", normalized_arr)