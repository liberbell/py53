import pandas as pd

list1 = [1, 2, 3, 4, 5]
print(list1)
list2 = [x**2 for x in list1]
print(list2)

sr = pd.Series(list2, index=list1)
print(sr)