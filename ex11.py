def computepay(h,r):
    if int(h)>40:
        z=r*1.5*h
    else:
        z=r*h
    return z
h=input('Please enter hours\n')
try:
    h=float(h)
except:
    h=-1
if h<0:
    print('Error, please enter numeric input')
r=input('Please enter rate\n')
r=float(r)
zp=computepay(h,r)
print('pay=',zp)
