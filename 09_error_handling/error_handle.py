
#1st method to open a file
file =open('youtube.txt','w')#opens the file if file not present creates the file then opens it

try:
  file.write('chai aur code')#writes the statement chai aur code inside the file
finally:
  file.close()#closes the file

  
#2nd method
with open('youtube.txt','w') as file
 file.write('chai aur python')