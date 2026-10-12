#print only the even num,bers of a list using a list comprehensions.
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

even_numbers = [x for x in list1 if x % 2 == 0]
print(even_numbers)
