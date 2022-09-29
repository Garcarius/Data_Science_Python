a=[1,2,3]
b=[4,5,6]
c=a+b #concatenar listas
print(c,'\n')
print(a,'\n')
#se puede dividir una lista usand [:]

print(c[:4]) #en la posicion 0 hasta 3 por que el numero final no se incluye

x=list()
#print(type(x))
#print(dir(x))
x.append('Darly') #Agrega al final de la lista
x.append('Adri')
print(x)
#x.append(89) # si se intenta agregar este valor dara error por el tipo de dato
print(x)
print(89 in x) #no existe este valor dara falso
print('Mau' in x) #no existe este valor dara falso
print(x.sort()) #lista organizada
print(sorted(x)) #lista organizada
print(x[1])


test=list()
while True:
    imp=input('Inserte el numero: ')
    if imp == 'done' : break
    val=float(imp)
    test.append(val) #Agrega al final de la lista
Ave=sum(test)/len(test)
print('el promedio es: ',Ave,'Maximo: ',max(test),'sumatoria: ',sum(test))
