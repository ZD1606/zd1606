sum=0
num=0
while True:
    h=input('Please enter score\n')
    if h=='done':
        break
    try:
        h=float(h)
    except:
        print('Bad score')
        continue
    sum=sum+float(h)
    num=num+1
    print(sum,num)
sr=sum/num
print('sum=',sum,'number=',num,'sr=',sr)
