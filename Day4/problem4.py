#Generate a 10 random integers from 1 to 100(seed7) and print mean,max min and the sorted array
import numpy as np

# Set seed for reproducibility
np.random.seed(7)

# Generate 10 random integers from 1 to 100
arr = np.random.randint(1, 101, size=10)

# Calculate stats
mean_val = np.mean(arr)
max_val = np.max(arr)
min_val = np.min(arr)
sorted_arr = np.sort(arr)

print("Generated Array:", arr)
print("Mean:", mean_val)
print("Max:", max_val)
print("Min:", min_val)
print("Sorted Array:", sorted_arr)