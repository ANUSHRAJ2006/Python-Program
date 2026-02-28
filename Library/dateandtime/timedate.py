import datetime as dt
print('Datetime:', dt.datetime.now())
print('Datetime Today:', dt.date.today())
date1=dt.date(2006,11,6)
date2=dt.date(2026,1,22)
diff=date2-date1
print(f'Different is:{diff.days}')
