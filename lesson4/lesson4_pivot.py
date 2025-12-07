import pandas as pd
import random
from scipy import stats
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np

print(["a", "b", "c"] + ["d", "e", "f"])
print(["a", "b", "c"] * 3)

p = ["osaka", "kyoto", "tokyo"] * 100
random.seed(1)
random.shuffle(p)
# print(p)

random.seed(2)
m = ["okoomi"] * 80 + ["curry"] * 120 + ["oden"] * 50 + ["udon"] * 50
random.shuffle(m)
# print(m)

df = pd.DataFrame()
df["comefrom"] = p
df["favorite"] = m
df["age"] = stats.norm.rvs(loc=35, scale=10, size=300, random_state=3).astype("int32")
print(df)

df2 = df.pivot_table(index="comefrom", columns="favorite", values="age", aggfunc="mean")
print(df2)

print(df[(df["comefrom"] == "osaka") & (df["favorite"] == "oden")]["age"].mean())

df2 = df.pivot_table(index="comefrom", columns="favorite", values="age", aggfunc="min")
print(df2)

df2 = df.pivot_table(index="comefrom", columns="favorite", values="age", aggfunc="max")
print(df2)

df2 = df.pivot_table(index="comefrom", columns="favorite", values="age", aggfunc="count")
print(df2)

print(pd.crosstab(df["comefrom"], df["favorite"], margins=True))

df2 = df.pivot_table(index="comefrom", columns="favorite", values="age", aggfunc="count", margins=True)
print(df2)

print(df)
sr = df["favorite"].value_counts()
# print(sr)

# sr.plot(kind="pie")
# plt.figure()
# plt.show()

sr.name = ""
# sr.plot.pie()
# plt.show()
# e = [0, 0, 0.2, 0]
# sr.plot.pie(startangle=90, counterclock=False, explode=e, autopct="%5.2f")
# plt.show()

e = [0, 0, 0.2, 0]
c = ["red", "green", "blue", "cyan"]
# sr.plot.pie(startangle=90, counterclock=False, explode=e, autopct="%5.2f%%", colors=c)
# plt.show()

x = np.arange(-6.3, 6.4, 0.3)
y1 = np.sin(x)
y2 = np.cos(x)
df3 = pd.DataFrame()
df3["x"] = x
df3["sin"] = y1
df3["cos"] = y2
print(df3.head(5))


# df3.plot(x="x", y=["sin", "cos"], lw=0.8)
# plt.title("graph of sin and cos")
# plt.grid()
# plt.xlim(-6, 6)
# plt.ylim(-1.2, 1.2)
# plt.show()

fname = r"data/GDP.csv"
# G = pd.read_csv(fname, index_col=0)
# print(G)
# G.plot(kind="bar", xlabel="country", ylabel="GDP", title="GDP 2021")
# plt.show()

x1 = stats.norm.rvs(loc=1, scale=1, size=200, random_state=1)
x2 = stats.norm.rvs(loc=8, scale=2, size=800, random_state=2)
x12 = np.append(x1, x2)
print(len(x12))

y1 = stats.norm.rvs(loc=1, scale=1, size=200, random_state=3)
y2 = stats.norm.rvs(loc=8, scale=2, size=800, random_state=4)
y12 = np.append(y1, y2)
print(len(y12))

df4 = pd.DataFrame()
df4["x"] = x12
df4["y"] = y12

# df4.hist(bins=20, figsize=(12, 3))
df4.plot(kind="scatter", x="x", y="y")
plt.show()
