dict_={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
day=input ("enter day\n")
month=input ("enter month\n")
year=input ("enter year")
countm=0
countd=0
p=0

if month[0]=='0':
  month=int(month [1])
  countm=1
if day[0]=='0':
  day=int(day [1])
  countd=1

if (int(year)%4==0 and int(month) ==2 and int(day)==29):
  day="01"
  month="03"
  countm=0
  countd=0
  p=1
if int (month)==12 and int (day)==31:
  month="01"
  year=int (year)+1
  day="01"
  countm=0
  countd=0
  p=1
if int(day)==int(dict_[int(month)]):
   day="01"
   month=int(month)+1
   countd=0
   p=1
if countm==1:
  month='0'+ str(month)

if countd==1:
  day='0'+ str(day)

if p==0:
  print (f"Day = {int(day)+1}")
  print (f"month = {month}")
  print (f"Year = {year}")

if p==1:
  print (f"Day = {day}")
  print (f"month = {month}")
  print (f"Year = {year}")