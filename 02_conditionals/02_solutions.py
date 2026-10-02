age=int(input("enter an appropriate age:"))
day=input("enter the day")
price= 12 if age >=18 else 8
if day=="wednesday":
  price=price-2
print("ticket price for you is $",price)
