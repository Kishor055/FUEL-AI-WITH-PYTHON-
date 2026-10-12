#Compare the time taken by a list and a Numpy array to add 1,000,000 numbers
import time
import numpy as np

size = 1_000_000

# 1. Python List Addition
list1 = list(range(size))
list2 = list(range(size))

start_time = time.time()
list_result = [x + y for x, y in zip(list1, list2)]
list_duration = time.time() - start_time

# 2. NumPy Array Addition
arr1 = np.arange(size)
arr2 = np.arange(size)

start_time = time.time()
numpy_result = arr1 + arr2
numpy_duration = time.time() - start_time

# Display Results
print(f"Python List time: {list_duration:.4f} seconds")
print(f"NumPy Array time: {numpy_duration:.4f} seconds")
print(f"NumPy is {list_duration / numpy_duration:.2f}x faster!")
