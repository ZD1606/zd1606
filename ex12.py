def computegrade(h):
    if h>1.0:
        return('Bad score')
    elif h>=0.9:
        return('A')
    elif h>=0.8:
        return('B')
    elif h>=0.7:
        return('C')
    elif h>=0.6:
        return('D')
    else:
        return('F')
h=input('Please enter score\n')
try:
    h=float(h)
except:
    print('Bad score')
    quit()
x=computegrade(h)
print(x)
