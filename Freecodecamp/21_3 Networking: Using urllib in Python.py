#Networking: Using urllib in Python
import urllib.request , urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())


print('\n')


fhand2 = urllib.request.urlopen('http://data.pr4e.org/authors.txt')
for line in fhand2:
    print(line.decode().strip())