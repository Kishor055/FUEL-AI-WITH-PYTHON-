#default argument is used when we want to give a default value to the parameter of the function. 
#If the user does not provide any value for that parameter, then the default value will be used.
def power (base, exp=2):
    return base ** exp 

print(power(2,3))
print(power(10))
