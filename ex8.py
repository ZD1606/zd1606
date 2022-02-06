h=input('Please enter score\n')
try:
    h=float(h)

except:
    print('Bad score')
    quit()
if h>1.0:
    print('Bad score')
elif h>=0.9:
    print('A')
elif h>=0.8:
    print('B')
elif h>=0.7:
    print('C')
elif h>=0.6:
    print('D')
else:
    print('F')
