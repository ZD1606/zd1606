ent=input('enter name fales\n')
try:
    text=open(ent)
except:
    if ent==('na na boo boo'):
        print('NA NA BOO BOO TO YOU - You have been punkd!')
        quit()
    print('error',ent)
    quit()
count=0
sim=0
for line in text:
    if line.startswith('X-DSPAM-Confidence:'):
        c=line
        count=count+1
        #print(count)
        #print(c)
        #проверка вывода правильных значений
        a=c.find(':')
        b=c[a+1:]
        sim=sim+float(b)
        sr=sim/float(count)
        print(b)
        #проіерка отсекания
print(sim)
print('sr=',sr)
