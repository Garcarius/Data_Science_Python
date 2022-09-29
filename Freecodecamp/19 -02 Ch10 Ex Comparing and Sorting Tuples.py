fpath='/media/Docs/test/'
fname = input('Enter the file name: ')
if len(fname) < 1 :
    fname = 'clown.txt'
rfname = fpath+fname #termina la ruta y archivo
hand=open(rfname) # lee el archivo

di=dict()
for lin in hand:
    lin = lin.rstrip()
    wds=lin.split() #convierte en lista
    for w in wds:
        di[w]=di.get(w,0)+1
#print(di)

tmp=list()
for k,v in di.items():
    d=(v,k)
    tmp.append(d)
ls=sorted(tmp,reverse=True)
for v,k in ls[:5]:
    print(k,v)

