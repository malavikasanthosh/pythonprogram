from datetime import datetime,timedelta,date

now=datetime.now()
current=now.time()
print("current time:",current)

dt=date.today()-timedelta(5)
print("current date:",date.today())
print("5 days before current date:",dt)

yest=date.today()-timedelta(1)
tom=date.today()+timedelta(1)
print("yesterday:",yest)
print("today:",date.today())
print("tommorrow:",tom)

for x in range(0,5):
  t=date.today()+timedelta(x)
print("Next 5 days from current date:",t)

a=datetime.now()
b=datetime.now()+timedelta(0,5)
print("current time:",a.time())
print("Time after adding 5 seconds",b.time())

