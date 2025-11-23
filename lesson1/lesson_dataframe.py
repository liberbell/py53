import pandas as pd

list1 = [[1, 1, 1], [2, 4, 8], [3, 9, 27]]
for x in list1:
    print(x)

df = pd.DataFrame(list1, columns=['linear', 'square', 'cubic'])
print(df)