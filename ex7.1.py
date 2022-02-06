h=input('Please enter hours\n')
try:
    h=float(h)
except:
    print('Error, please enter numeric input')
    quit()
r=input('Please enter rate\n')
try:
    r=float(r)
except:
    print('Error, please enter numeric input')
    quit()
if int(h)>40:
    z=r*1.5*h
else:
    z=r*h
print('pay=',z)
