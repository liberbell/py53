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

d1 = pd.Timestamp("2000-01-01T00:00:00", tz="Asia/Tokyo")
d2 = pd.Timestamp("2022-03-14T13:15:00", tz="Asia/Tokyo")
td21 = d2 - d1
print(td21)

td100 = pd.Timedelta("100 days 01:20:30")
print(td100)

td100 = pd.Timedelta(days=100, hours=1, minutes=20, seconds=30)
print(td100)

d1 = pd.Timestamp("2022-01-01T00:00:00")
d2 = pd.Timestamp("2022-12-31T23:59:59")

dr = pd.date_range(d1, d2, freq="MS")
print(dr)

dr = pd.date_range(d1, d2, freq="D")
print(dr)