import pandas as pd
from scipy import stats

# print(stats.uniform.rvs(size=5, random_state=3))

df = pd.DataFrame()
df["Uni"] = stats.uniform.rvs(size=10000)
df["Norm"] = stats.norm.rvs(size=10000)
print(df)