from datetime import datetime,timedelta
today=datetime.today()
future=today+timedelta(days=10)
past=today-timedelta(days=5)
print('Future:',future)
print('Past:',past)
