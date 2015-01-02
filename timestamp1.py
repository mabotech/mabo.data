


import time
import datetime

# influxdb timestamp check

# CentOS: date --set="4 Jan 2015 13:29:00"

s = 1420319220000

s = time.time()*1000

s = 1420350177000

s1 = s/1000




print(
    datetime.datetime.fromtimestamp(
        int(s1)
    ).strftime('%Y-%m-%d %H:%M:%S')
)