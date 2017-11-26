import time
date1 = "31/12/2015"
newdate1 = time.strptime(date1, "%d/%m/%Y")
print(newdate1)
date2="2018/11/15"
newdate2=time.strptime(date2,"%Y/%m/%d")
print(newdate2)


import datetime

a=datetime.date(2017,11,13)
print(a)


b=HotelData.objects.filter(checkin_date__gte=a)