import sympy
import pandas as pd
p = list(sympy.primerange(1, 100))
p_num = len(p)
print(len(p))

list1 = list(range(1, p_num + 1))
sp = pd.Series(p, index=list1)
print(sp)