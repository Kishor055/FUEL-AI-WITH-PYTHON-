#local:created inside a function and can be used only inside that function
#Global:created outside a function and can be used anywhere in the program
x = 10 #global variable
def show():
    y = 20 #local variable
    print(x,y)

show()
#print(y) #this will give error because y is local variable and can be used only inside the function
print(x) #this will work because x is a global variable

