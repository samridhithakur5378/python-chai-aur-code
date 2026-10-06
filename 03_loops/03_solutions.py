n=int(input("enter a valid in number"))
for i in range(1,11):
  if i==5:
    continue
  print(n ,'*', i,'=', n*i)