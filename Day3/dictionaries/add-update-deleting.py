student = {
    "Name" : "Kishor",
    "age" : 23,
    "city" : "pune"
 }

student["course"] = "python"
student["age"] = 24
student.update({"city":"Kolhapur"})

student.pop("age")
print(student)