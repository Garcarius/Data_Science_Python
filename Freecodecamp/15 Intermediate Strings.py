word = "bananana"
i = word.find("na")
x=word.count('na')
print(i)
print(x)
print('--------')
s = 'Monty Python'
print('la expresion es: ',s)
print(len(s),'longitud')
print(s[0:4],'de 0 a 4')  # Imprime desde la posicion 0 hasta la 4
print(s[6:7],'de 6 a 7')
print(s[6:12],'de 6 a 12')
print(s[6:],'uno')
print(s[:6],'dos')
print('--------')
a = 'Hello'
b = a + 'there'
print(b)
c = a + ' ' + 'There'
print(c)
print('--------')
# in puede ser un operador logico
fruit = 'banana'
if 'n' in fruit:

    print('yes')
d=s.lower()
print(d)
print('WHATAGATAPITUSBERRY'.capitalize())
print('WHATAGATAPITUSBERRY'.lower()) #agregando metodos de cadenas a la cadena directamente se hace el cambio en el print