#Regular Expressions: Practical Applications

import re
fpath='/media/Docs/Cursos/Python/Python_Scrips/FreeCodeCamp/Test_src/'
fl='mbox-short.txt'
hand=open(fpath+fl)
numlist=list()
for line in hand:
    line=line.strip()
    stuff=re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line) # busca las palabras que comienzen con x-ds.. y despues de esa parte extraiga la cifas 
    if len(stuff)!=1: continue
    num=float(stuff[0])
    numlist.append(num)
print('Maximum',max(numlist),'Minimun',min(numlist))

print('\n')

x='We just recieved $10.000 for cookies.'
y=re.findall('\$[0-9.]+',x) #extrae el valor que comienza con $ y tenga una cifra
print(y) 