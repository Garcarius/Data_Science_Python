from os import path #para poder leer docs locales

print("Ini Ex1\n")
Path='/media/Docs/Cursos/Python/Python_Scrips/FreeCodeCamp/Test_src/'
file_n='linux.txt'
file_n2="mbox-short.txt"
fullfile=Path+file_n2

xfile =open(fullfile) #para abrir archivos
count=0
for lines in xfile: #Recorre cada linea de un archivo
    print(lines) #cada linea es asignada a la variable lines
    count=count+1
print('line count: ',count)
print("End Ex1\n")

print("Ini Ex2\n")
fhand = open(fullfile)
inp = fhand.read() # .read() para leer las lineas
print('\n'+str(len(inp))+'\n') #convierte y cuenta el numero de caracteres en el archivo
print(inp[:10]) #imprime la posicion 0 a 9 del archivo
print("End Ex2\n")

print("Ini Ex3\n")
xfile =open(fullfile)
for line in xfile:
    line=line.strip() # elimina los espacios
    if not line.startswith('https'): #funcion para buscar lineas que comiencen ej "https"
        continue #se salta la linea que cumppla la condicion
    print(line)
print("End Ex3\n")

#para leer distintos archivos    
print("Ini Ex4\n")
fname = input('Enter the file name: ')
pathf=Path
rfile=pathf+fname
try: #para evitar nombres incorrectos
    fhand=open(rfile)
except:
    print('file cannot be opened',fname)
    quit() #sale de todo el scritp
count=0
for line in fhand:
    if line.startswith('Received'): #modulo que cuando comienza con las palabras del parametro da verdadero
        count=count+1
print('there were',count,'subject lines in',fname)