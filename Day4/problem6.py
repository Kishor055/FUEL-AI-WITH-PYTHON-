#Find the Mean and standard deviations of an array of the marks.
import numpy as np

marks = np.array([85, 90, 78, 92, 88, 76, 95])

# Calculate Mean and Standard Deviation
mean_marks = np.mean(marks)
std_marks = np.std(marks)

print("Marks:", marks)
print("Mean:", mean_marks)
print("Standard Deviation:", std_marks)