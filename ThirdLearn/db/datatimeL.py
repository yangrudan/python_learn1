"""
Copyright (c) Zhejiang Lab. All right reserved.
"""


import datetime

time_str = "2021-02-06"
format_str = "%Y-%m-%d"
dt = datetime.datetime.strptime(time_str, format_str)

if dt.month+1 != 13:
    dt2 = datetime.datetime(year=dt.year, month=dt.month+1, day=1)
else:
    dt2 = datetime.datetime(year=dt.year, month=1, day=1)

res = dt2.strftime(format_str)


print(dt)
print(dt2)
print(res)

