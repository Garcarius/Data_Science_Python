#funcion para decir el numero de horas
def payment(hours,rate):
    print('In Automatic pay ', hours,rate)

sh = input('Enter hours: ')
sr  = input('Enter rate: ')
try:
    fh = float(sh)
    fr = float(sr)
except:
    print('Error,Input numeric values')
    quit() #Esto hace que se salga del codigo

payment(fh,fr)
if fh > 40: #Esto solo sera ejecutado si el try va bien
    rg=fh*fr  #Calculo de horas regulares
    ov=(fh-40)*(fr*1.5) #calculo de horas extras
    print('Overtime hours',fh-40)
    ovp=rg+ov  #sueldo con horas extras
    print('Your pay is ',ovp)
else:
    print('Regular') 
    py=fh*fr #pago regular
    print('Your pay is ',py)