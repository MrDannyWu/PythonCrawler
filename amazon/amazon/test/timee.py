import datetime
import time


print(datetime.datetime(2009, 3, 23))
t_str = '2012-03-05 16:26:23'
d = datetime.datetime.strptime(t_str, '%Y-%m-%d %H:%M:%S')
print(d)

dt1 = datetime.datetime.fromtimestamp(1565190102)
dt2 = datetime.datetime.fromtimestamp(1569078102)
print(str(dt1))
print(dt2)
print((dt2-dt1).days)