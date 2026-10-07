def is_even(num):
    return num %2 == 0

def factorial(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

print(is_even(4))#TRUE
print(is_even(5))#FALSE
print(factorial(5))#120
