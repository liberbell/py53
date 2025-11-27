import pandas as pd

list1 = [[1, 1, 1], [2, 4, 8], [3, 9, 27]]
df = pd.DataFrame(list1, index=["d1", "d2", "d3"], columns=["linear", "square", "cubic"])
print(df)

dname = r"data"
fname1 = dname + r"/csv01.csv"
# print(fname1)

df.to_csv(fname1)

fname2 = dname + r"/csv01_noindex.csv"
df.to_csv(fname2, index=False)

fname3 = dname + r"/csv01_nohead.csv"
df.to_csv(fname3, header=False)

df2 = pd.read_csv(fname1)
print(df2)

df2 = pd.read_csv(fname1, index_col=0)
print(df2)

df2 = pd.read_csv(fname2)
print(df2)

df2 = pd.read_csv(fname3, index_col=0, names=["linear", "square", "cubic"])
print(df2)