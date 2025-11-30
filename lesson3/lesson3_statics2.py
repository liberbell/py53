import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.DataFrame()
df["Norm"] = stats.norm.rvs(loc=0, scale=1, size=10000)
df["LogNorm"] = stats.lognorm.rvs(loc=0, s=1, size=10000)
df.hist(bins=20)
print(df.describe())
plt.plot(df)
# plt.show()

B = df["Norm"].value_counts(bins=20)
print(B)
B.sort_index(inplace=True)
print(B)
print(B.index[0])