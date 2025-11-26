import pandas as pd

list1 = [[1, 1, 1], [2, 4, 8], [3, 9, 27]]
df = pd.DataFrame(list1, index=["d1", "d2", "d3"], columns=["linear", "square", "cubic"])
print(df)

dname = r"/data"
fname = dname + r"/csv01.csv"
print(fname)