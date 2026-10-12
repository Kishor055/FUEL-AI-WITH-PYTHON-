#DataFrames from a dict
import pandas as pd

df=pd.DataFrame({
    "name": ["Riya", "Aman","Neha",
             "Karan", "Isha", "Rohan"],
    "city" : ["Pune","Mumbai","Pune",
              "Kolhapur","Mumbai","Pune"],
    "marks" : [ 85, 62, 91, 45, 78, 70],
    "attendances" : [ 92, 75, 68, 84, 98, 89],
})

print(df)
    