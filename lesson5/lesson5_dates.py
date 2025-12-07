import pandas as pd

d1 = pd.Timestamp.now()
print(d1)
# d2 = pd.Timestamp.now(tz="Asia/Tokyo")
d2 = pd.Timestamp.now(tz="Europe/London")
print(d2)