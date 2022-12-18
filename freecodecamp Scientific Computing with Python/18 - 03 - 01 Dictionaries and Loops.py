#Dictionaries and Loops
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])


#09 - EX
fpath='/media/Docs/Cursos/Python/Python_Scrips/FreeCodeCamp/Test_src/'
fname = input('Enter the file name: ')
if len(fname) < 1 :
    fname = 'clown.txt'
rfname = fpath+fname #termina la ruta y archivo
hand=open(rfname) # lee el archivo

di=dict()
for lin in hand:
    lin = lin.strip()
   # print(lin)
    wds=lin.split() #convierte en lista
    #print(wds) 
    for w in wds:
        print('**',w,di.get(w,'**'))
        if w in di:
            di[w]=di[w]+1 #contador 
        else:
            di[w]=1
            #print('***New***')
        print(w,di[w])