#series in pandas
import pandas as pd
s = pd.Series([10,20,30], index=["a","b","c"])

print(s)

print(s["b"])#20
print(s.mean())#20.0
