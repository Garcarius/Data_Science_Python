abc ='With three words'
stuff=abc.split()#separa la cadena por una lista que se separo por espacios
print(stuff)
print(stuff[0])
for w in stuff:
    print(w)

line='Hola ;como;estas'
ho=line.split(';') #tambien acepta parametos de separacion
print(ho)

#cuando no se especifica un delimitador , toma los espacios como delimitador

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split() #separa espacios
parts = pieces[3].split('-') #toma la posicion 3 de la lista y la separa por '-'
n = parts[1] #asigna primera posicion de la lista
print(n)

