#Regular Expressions: Matching and Extracting Data

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s) #busca cadenas que tengan @ pero que no tengan espacio adelante y al final incluye @
lst1 = re.findall('@\S+', s) #busca palabras que tengan @ y no etanga espacio al lado incluye @
lst2 = re.findall('@(\S+)', s)# busca las cadenas donde comiencen con @ y sin espacios despues sin incluir
print(lst)
print(lst1)
print(lst2)