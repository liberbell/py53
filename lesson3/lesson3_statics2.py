import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.DataFrame()
df["Norm"] = stats.norm.rvs(loc=0, scale=1, size=10000)
df["LogNorm"] = stats.lognorm.rvs(loc=0, s=1, size=10000)
df.hist(bins=20)
print(df.describe())
plt.plot(df)
plt.show()