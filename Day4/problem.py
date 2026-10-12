#Create an array of the numbers 1 to 20 and print only the even number 
import numpy as np 

# Create an array of numbers from 1 to 20
arr = np.arange(1, 21)

# Filter and print only even numbers
even_numbers = arr[arr % 2 == 0]
print(even_numbers)

"""OUTPUT : [ 2  4  6  8 10 12 14 16 18 20]"""


