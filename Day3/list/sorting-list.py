marks = [15,45,78,33,50]
marks.sort()
print(marks)#15,33,45,50,78
marks.sort(reverse=True)#reverse the list
print(marks)
marks.reverse()
print(33 in marks)#True
print(marks.count(45))#1
print(marks.index(78))#index of the 78
