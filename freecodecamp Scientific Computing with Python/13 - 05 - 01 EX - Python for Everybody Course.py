print('five')
num = 0
tot=0.0
while True:
    sval= input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval=float(sval)
    except: #en caso de error esto funciona para hacer una excepcion y continuar
        print('Invalid input')
        continue
    num = num + 1
    tot = tot + fval

print('total of numbers',num,'total',tot,'Average',tot/num)