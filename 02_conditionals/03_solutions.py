score=int(input("enter a valid score"))

if score>=101:
  print("please verify your grade again")
  exit()
  
if score>=90:
  print("A grade")
elif score<90 and score>=80:
  print("B grade")
elif score<80 and score>=70:
  print("C grade")
elif score<70 and score>=60:
  print("D grade")
else:
  print("f grade")