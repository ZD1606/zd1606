sum=0
num=0
small=None
big=None
while True:
    h=input('Please enter score\n')
    if h=='done':
        break
    try:
        h=float(h)
    except:
        print('Bad score')
        continue
    if small is None:
        small=h
    elif small>h:
        small=h
    if big is None:
        big=h
    elif big<h:
        big=h
    sum=sum+float(h)
    num=num+1
    print(sum,num,small,big)
print('sum=',sum,'number=',num,'Least=',small,'largest',big)
