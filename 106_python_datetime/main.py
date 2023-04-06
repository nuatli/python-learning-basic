import datetime

mytime = datetime.time()
print(mytime)

mytime = datetime.time(2,20)
print(mytime)

mytime = datetime.time(13,20,1,20)
print(mytime)

today = datetime.date.today()
print(today)
print(today.ctime())
print(today.ctime().split())

'''
today.year,today.month,today.day
'''


from datetime import datetime

mydatetime = datetime(2021,10,3,14,20,1)
print(mydatetime)

mydatetime = mydatetime.replace(year=2020)
print(mydatetime)


from datetime import date

date1 = date(2021,11,3)
date2 = date(2020,11,3)

result = date1 - date2

type(result)

print(result.days)

datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)
result_datetime = datetime1 - datetime2

print(result_datetime)
