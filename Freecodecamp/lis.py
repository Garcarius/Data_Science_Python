d={'c':22,'b':1,'a':20}
t= sorted(d.items())
temp=list()
print(t)
for k,v in sorted(d.items()):
  temp.append((v,k))
print(temp)
temp=sorted(temp,reverse=True)
print(temp)