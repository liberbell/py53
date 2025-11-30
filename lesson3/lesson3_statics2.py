import pandas as pd
from scipy import stats

df = pd.DataFrame()
df["Norm"] = stats.norm.rvs(loc=0, scale=1, size=10000)

print(df)