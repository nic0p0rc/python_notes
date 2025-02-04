from datetime import datetime, timedelta

now=datetime.now()
print(now)

data1= datetime(2024,6,18)
data2= datetime(2024,7,22)
difference = data2-data1
print(difference.days)