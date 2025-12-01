import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame()
df["Norm"] = stats.norm.rvs(loc=0, scale=1, size=10000)
df["LogNorm"] = stats.lognorm.rvs(loc=0, s=1, size=10000)
# df.hist(bins=20)
# print(df.describe())
# plt.plot(df)
# plt.show()

B = df["Norm"].value_counts(bins=20)
# print(B)
B.sort_index(inplace=True)
# print(B)
# print(B.index[0])
# print(B.max())

# iv = pd.Interval(1, 2, closed="neither")
# print(iv)

x = np.arange(-2, 2, 0.05)
# print(x)

y = x**2
# print(y)

fname = r"data/" + "testFig01.png"

# plt.figure()
# plt.plot(x, y)
# plt.savefig(fname)
# plt.show()

fname = r"data/" + "testFig02.png"

# plt.figure()
# df.hist(bins=20, figsize=(14, 3))
# plt.savefig(fname)

fname = r"data/" + "testFig03.png"
plt.figure()
df["Norm"].hist(bins=30, alpha=0.6)
df["LogNorm"].hist(bins=30)
plt.savefig(fname)
