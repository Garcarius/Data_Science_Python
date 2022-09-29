#from typing import Counter


#lst = []
#for key, val in Counter.items():
   # newtup = (val, key)
  #  lst.append(newtup)
#lst = sorted(lst, reverse=True)
#print(lst)


d={'c':22,'b':1,'a':20}
#print(d.items())
#print(sorted(d.items()))
tmp=list()
for k, v in d.items():
  tmp.append((v,k))
print(sorted(tmp)) #sorted debe estar como funcion separarada

fpath='/media/Docs/Cursos/Python/Python_Scrips/FreeCodeCamp/Test_src/'
fname='romeo.txt'
file=fpath+fname
fahnd=open(file)
counts=dict()
for line in fahnd: #contar repeticiones
  words = line.split() #separar las lineas
  for word in words: #get es para saber existencia
    counts[word] = counts.get(word,0)+1

lst=list()
for k, v in counts.items(): #extrae los valores del diccionario
  newtup=(v,k) #crea una tupla con valores invertidos
  lst.append(newtup) #anexa la tupla a una lista

lst=sorted(lst,reverse=True) #invierte el orden desc

for v,k in lst[:10]: # toma los 10 primeros
  print(k,v)


  print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )

