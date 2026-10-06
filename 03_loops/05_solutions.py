input_str= "teeter"
for char in input_str:
  print(char)
  if input_str.count(char)==1:
   print("char is : ",char)
   break#The break keyword in Python is used to terminate a loop immediately when a specific condition is met, tr


#imp note
#Break exits the entire loop permanently.  Once encountered, it stops all remaining iterations and moves control outside the loop structure.
#Continue skips the current iteration only.  It ignores the remaining code in the current cycle but keeps the loop running for subsequent items.