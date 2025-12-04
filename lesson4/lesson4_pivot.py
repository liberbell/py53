import pandas as pd
import random
from scipy import stats
import matplotlib.pyplot as plt
import japanize_matplotlib

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
e = [0, 0, 0.2, 0]
sr.plot.pie(startangle=90, counterclock=False, explode=e, autopct="%5.2f")
plt.show()