#Keyword arguments allow you to specify the values of function parameters by name, rather than by position.
# This can make your code more readable and allows you to provide arguments in any order.
name = input("Enter Your Name : ")
city = input("Enter Your City : ")
def intro (name, city):
    print(f"{name} is from {city}")

# Calling the function with keyword arguments
intro(name=name, city=city)  # Using variables as keyword arguments
intro(name="riya", city="New York")
intro(city="Los Angeles", name="RAM")  # Order doesn't matter when using keyword arguments


