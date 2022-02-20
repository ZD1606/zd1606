
library=dict()
ent=open('text.txt')
enter=ent.read()
enter=str(enter)
char=""
for x in enter:
    if x.isalpha():
        char="".join([char,x])
#print(char)
for y in char.lower():
    library[y]=library.get(y,0)+1
#print(library)
words=[]
for let,count in library.items():
    newlist=(count,let)
    words.append(newlist)
    words=sorted(words,reverse=True)
for count,let in words :
    print(let,count)
