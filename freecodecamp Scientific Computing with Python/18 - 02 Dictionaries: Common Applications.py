#Dictionaries: Common Applications
#from typing import Counter
#from collections import Counter
counts=dict()
counts_2=dict()
names = ['Holi','0','csev','mrugesh','csev','0','csev','xd']
for name in names:
    counts_2[name]=counts_2.get(name,0)+1 #si encuentra el nombre, da el valor y le suma 1, en caso contrario seria 0 + 1
    if name not in counts:
        counts[name]=1
    else:
        counts[name]+=1
print(counts,'\n')
print(counts_2)

counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))