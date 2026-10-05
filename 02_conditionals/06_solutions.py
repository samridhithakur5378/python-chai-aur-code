dist=int(input('enter a valid distance'))
if dist<3:
  transport='walk'
elif dist>=3 and dist<=15:
  transport='bike'
else:
  tansport ='car'
print('ai recomments you the transport of:',transport)
