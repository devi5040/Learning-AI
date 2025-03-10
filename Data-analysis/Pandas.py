import pandas as pd
# creating the series
data = [1,2,3,4,5]
series = pd.Series(data)
print(series)

# custom index
a = [10, 20, 30, 40, 50]
b = ['hello','hi','good','thanks','cool']
s = pd.Series(b,index=a)
print(s)