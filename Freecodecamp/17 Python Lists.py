#Estructuras -- Listas!!!!
fruit="banana"
print(fruit[1],'\n') #las lista comienzan desde la posicion 0
for i in fruit:
    print(i)
print("\nEnd!\n")


Chat=['Darly','Silvi','Hada','Adri']
for x in Chat:
    print('feliz año nuevo',x.upper(),'\n')
print('Done') 
a="0" 
print(len(Chat))
r=range(5)
print(r,"\n")
for i in r:
    a=a+"+"+str(i)
    print(i)
    print(a)

    Chat=['Liah','Nicolas','Maleja','Adri']
for x in range(len(Chat)): #los indices siempre deben ser numericos
   mess = Chat[x].upper() #para que acepte la posicion
   print('feliz año nuevo',mess,'\n')
print('Done') 