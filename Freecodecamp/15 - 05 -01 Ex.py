num = 0
tot = 0
max=None
min=None
while True :
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval=float(sval)
        num=num+1
        tot=tot+fval
        if min is None or fval < min :
            min = fval
        if max is None or fval > max:
            max = fval
    except: #en caso de error esto funciona para hacer una excepcion y continuar
        print('Invalid input')
        continue
print('Total is: ',tot,'numbers: ',num,'average: ',tot/num,'num max: ',max,'min num: ',min)
