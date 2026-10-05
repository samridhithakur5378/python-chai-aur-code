password = input("enter the valid password:")
if len(password) < 6:
  strength="weak"
elif len(password)>=6 and len(password)<=10:
  strenth="medium"
else:
  strength="strong"

print("password strength is",strength)