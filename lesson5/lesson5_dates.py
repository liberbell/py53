import pandas as pd

d1 = pd.Timestamp.now()
print(d1)
# d2 = pd.Timestamp.now(tz="Asia/Tokyo")
d2 = pd.Timestamp.now(tz="Europe/London")
print(d2)
print(d2.year)
print(d2.month)
print(d2.day)
print(d2.hour)
print(d2.minute)
print(d2.second)
print(d2.microsecond)
