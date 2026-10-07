#Returning many values from a fuction is possible in python.
#You can return multiple values from a function by separating them with commas.
# When you call the function, you can unpack the returned values into separate variables. 
a = int(input("enter a number :"))
b = int(input("enter a number :"))

def min_max(a, b):
    return min(a, b), max(a, b)

low, high = min_max(a,b)
print("low,high :", low, high)

