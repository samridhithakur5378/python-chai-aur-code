number= int(input("enter a valid number"))
factorial = 1

while number>0:
  factorial = factorial * number
  number= number-1
print("factorial:",factorial)