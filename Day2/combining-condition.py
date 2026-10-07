age = int(input("Enter your Age:"))
has_id = input("Enter you Have ID :")

if age >= 18 and has_id:
    print("Entry Allowed")
if age < 13 or age > 60 :
    print("Discounted")
if not has_id:
    print("ID Requird")
else :
    print("Carry Your ID Proof")           