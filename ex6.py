h=input('Please enter hours\n')
h=float(h)
r=input('Please enter rate\n')
r=float(r)
if int(h)>40:
    z=r*1.5*h
else:
    z=r*h
print('pay=',z)
