import pandas as pd

list1 = [1, 2, 3, 4, 5]
print(list1)
list2 = [x**2 for x in list1]
print(list2)

sr = pd.Series(list2, index=list1)
print(sr)

sr0 = pd.Series(list2)
print(sr0)
print(sr.at[1])
print(sr.loc[1:3])
sr.at[2] = 999
print(sr)
sr.loc[2:4] = [10, 20, 30]
print(sr)

words = pd.Series(["Apple", "Orange", "Melon"], index=["a", "b", "c"])
print(words)
print(words.at["a"])

words.watrmelon = "watermelon"
print(words)

words.at["w"] = "Water melon"
print(words)

words.w = "Watermelon"
print(words)

print(sr.iat[0])
print(sr.iloc[1:3])

lst = ["a", "b", "c", "d", "e"]
print(lst[0])

sr01 = pd.Series([2, 4, 6, 8, 10], index=[0, 1, 2, 3, 4])
sr02 = pd.Series([2, 4, 6, 8, 10], index=[1, 2, 3, 4, 5])
print(sr01, sr02)
print(sr01[0:3])
print(sr02[0:3])

msk = [True, True, False, True, False]
print(sr)
print(sr.iloc[msk])
print(sr < 10)