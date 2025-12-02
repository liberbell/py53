import pandas as pd
import random
from scipy import stats

print(["a", "b", "c"] + ["d", "e", "f"])
print(["a", "b", "c"] * 3)

p = ["osaka", "kyoto", "tokyo"] * 100
random.seed(1)
random.shuffle(p)
print(p)

random.seed(2)
m = ["okoomi"] * 80 + ["curry"] * 120 + ["oden"] * 50 + ["udon"] * 50
random.shuffle(m)
print(m)