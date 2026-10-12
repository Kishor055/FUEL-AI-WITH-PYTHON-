# names = ["Riya","Aman","neha"]

# with open("names.txt", "w") as f:
#     for n in names:
#         f.write(n +"\n")
   
#input from the user
namesi = input("Enter your name : ") 
names = list(namesi.split())
with open("names.txt", "w") as f:
    for n in names:
        f.write(n)