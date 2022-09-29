import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip()) #decodifica el utf-8 y le quita los espacios para imprimirlos en pantalla
    

print('\n')

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1 #asigna un valor a la palabra que esta contando en caso de no existir le agrega un y le suma uno, de lo contrario le suma uno al valor ya encontrado
print(counts)    