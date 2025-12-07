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
print(d2.weekday())

d3 = pd.Timestamp("1966-03-14T13:15:00+09:00")
print(d3)

d3 = pd.Timestamp("1966-03-14T13:15:00", tz="Asia/Tokyo")
print(d3)

d3 = pd.Timestamp("19660314131500", tz="Asia/Tokyo")
print(d3)

d3 = pd.Timestamp("1966-03-14T04:15:00Z")
print(d3)

print(d3.tz_convert("Asia/Tokyo"))