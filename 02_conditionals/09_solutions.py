year=int(input("enter a valid year:"))
if (year%400==0)  or year%4==0 and year%100!=0:
  print(year,"the year is leap")
else:
  print("year is not a leap year")

