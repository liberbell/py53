import pandas as pd
import numpy as np

list1 = [[1, 1, 1], [2, 4, 8], [3, 9, 27]]
# for x in list1:
#     print(x)

df = pd.DataFrame(list1, columns=['linear', 'square', 'cubic'], index=['d1', 'd2', 'd3'])
print(df)

df = pd.DataFrame(list1, columns=['linear', 'square', 'cubic'])
print(df)

df = pd.DataFrame(list1)
print(df)

ar = np.array(list1)
print(ar)

df = pd.DataFrame(ar, columns=['linear', 'square', 'cubic'])
print(df)

dc = {"linear": [1, 2, 3], "square": [1, 4, 9], "cubic": [1, 8, 27]}
print(dc)
df = pd.DataFrame(dc, index=["d1", "d2", "d3"])
print(df)

df2 = pd.DataFrame()
df2.at["d1", "linear"] = 1
df2.at["d1", "square"] = 1
df2.at["d1", "cubic"] = 1
df2.at["d2", "linear"] = 2
df2.at["d2", "square"] = 4
df2.at["d2", "cubic"] = 8
df2.at["d3", "linear"] = 3
df2.at["d3", "square"] = 9
df2.at["d3", "cubic"] = 27
print(df2)

df3 = pd.DataFrame()
df3.at["d1", "linear"] = 1
df3.at["d2", "square"] = 4
df3.at["d3", "cubic"] = 27
print(df3)
df31 = df3.fillna(0)
print(df31)

print(df2.iat[2, 1])
print(df2)
print(df2.loc["d1":"d2", "linear":"square"])
print(df2.loc["d1":"d2", :])
print(df2.loc[:, "linear":"square"])
print(df2.loc[["d1", "d3"], ["linear", "cubic"]])

print(df2.iloc[0:2, 0:2])
print(df2.iloc[[0, 2], [0, 2]])

print(df2["linear"])

c = pd.Series(["Eric", "Elton", "Bob"], index=["d1", "d2", "d3"])
df2["name"] = c
print(df2)

print(df2[["linear", "name"]])

df3 = pd.DataFrame([[1, 2], [3, 4]])
print(df3)
df4 = pd.DataFrame([["Eric", "UK", 80], ["Bob", "CB", 45]], columns=["name", "nationality", "age"])
print(df4)
print(df4.name)