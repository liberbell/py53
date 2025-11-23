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