#generator function( do your own research too)
def even_generator(limit):
  for i in  range(2,limit+1,2):
    yield i #yield keyword
  

for num in even_generator(10):
  print(num)