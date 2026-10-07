# swap two numbers
a,b,c,d = 1,2,3,4
a,b = b,a
print(a,b,c,d)
print(type(a))

#SWAP TWO NUBER USING THIRD VAR
a = 10
b = 20
print(f"before swapping a={a} b={b}")
c = a
a = b
b = c
print(f"after swapping a={a} b={b}")

#SWAP TWO NUBER without THIRD VAR
a = 10
b = 20
print(f"before swapping a={a} b={b}")
a, b = b, a
print(f"after swapping a={a} b={b}")
