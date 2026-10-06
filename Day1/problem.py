# #print your name, college, and city  on three separate line
# name = input("Enter Your Name:")
# college = input("Enter your College:")
# city = input("Enter your city:")

# print(name)
# print(city)
# print(college)

# print(f"Name:{name}")
# print(f"City:{city}")
# print(f"College:{college}")

# num1 = int(input("Enter Your Number :"))
# num2 = int(input("Enter your Second Number :"))
# print(num1)
# print(num2)
# print(f"add:{num1+num2} \n Sub: {num1-num2} \n mul:{num1*num2}")
# print(f"Square:{num1*num1} \n Square:{num2*num2} \n Cube:{num1*num1*num1} \n Cube:{num2*num2*num2}" )

# #CONVERT 150 MINUTES INTO HOURS AND MINUTES USING // AND &
# minutes = 155
# print(f"Hours:{minutes//60} \n Minutes:{minutes%60}")


# #ASK FOR THE TEMPERATURE IN CELSIUS AND CONVERT IT INTO FAHRENHEIT (F=C*9/5+32)
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius}°C is equal to {fahrenheit}°F")

# #SWAP TWO NUBER USING THIRD VAR
# a = 10
# b = 20
# print(f"before swapping a={a} b={b}")
# c = a
# a = b
# b = c
# print(f"after swapping a={a} b={b}")

# #SWAP TWO NUBER without THIRD VAR
# a = 10
# b = 20
# print(f"before swapping a={a} b={b}")
# a, b = b, a
# print(f"after swapping a={a} b={b}")

#Check if a number entered by the user is greater than 15 then print true and if it is less than 15 then print false
number = int(input("Enter a number: "))
if number > 15 :
    print("True")
else:
    print("False")
    