#Convert the tempreature [0,20,37,100] from celsius to Fahrenheit in one line.
import numpy as np

fahrenheit = np.array([0, 20, 37, 100]) * 9/5 + 32
print(fahrenheit)