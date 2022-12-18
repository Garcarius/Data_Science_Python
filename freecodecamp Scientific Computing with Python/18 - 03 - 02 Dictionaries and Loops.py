#09 - EX
fpath='/media/Docs/Cursos/Python/Python_Scrips/FreeCodeCamp/Test_src/'
fname = input('Enter the file name: ')
if len(fname) < 1 :
    fname = 'clown.txt'
rfname = fpath+fname #termina la ruta y archivo
hand=open(rfname) # lee el archivo

di=dict()
for lin in hand:
    lin = lin.strip() #quita espacios
    wds=lin.split() #convierte en lista
    for w in wds:
        #si la llave no existe es 0 y le sumas 1
        di[w]=di.get(w,0)+1
        print(w,'***',di[w])
print(di)
largest=-1
word=None 
for v,k in di.items():
    if k>largest:
        largest=k
        word=v
print('The max val is ','value',largest,'with the word',word)