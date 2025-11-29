import pandas as pd
from scipy import stats

# print(stats.uniform.rvs(size=5, random_state=3))

df = pd.DataFrame()
df["Uni"] = stats.uniform.rvs(size=10000)
df["Norm"] = stats.norm.rvs(loc=0, scale=1, size=10000)
df["LogNorm"] = stats.lognorm.rvs(loc=0, s=1, size=10000)
print(df)

print(df["Uni"].hist())