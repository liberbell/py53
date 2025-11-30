import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# print(stats.uniform.rvs(size=5, random_state=3))

df = pd.DataFrame()
df["Uni"] = stats.uniform.rvs(size=10000)
df["Norm"] = stats.norm.rvs(loc=0, scale=1, size=10000)
df["LogNorm"] = stats.lognorm.rvs(loc=0, s=1, size=10000)
print(df)

# plt.plot(df["Uni"])
# df["Uni"].plot()
# plt.show()

# df["Norm"].plot()
# plt.show()

# df["LogNorm"].plot()
# plt.show()

r = df.describe()
print(r)

print(r.loc["mean", "Norm"])
print(r.loc["mean"])

sr = pd.Series(["a", "b", "b", "c", "c", "c"])
print(sr.value_counts())
print(sr.mode())

df = pd.DataFrame()
df["col1"] = sr
df["col2"] = ["a", "b", "b", "b", "c", "c"]
df["col3"] = ["b", "b", "b", "c", "c", "c"]
print(df["col3"].value_counts())
print(df.mode())