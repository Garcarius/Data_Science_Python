sh = input('Enter hours: ')
sr  = input('Enter rate: ')
fh = float(sh)
fr = float(sr)

if fh > 40:
    print('Overtime')
    rg=fh*fr  #Calculo de horas regulares
    ov=(fh-40)*(fr*1.5) #calculo de horas extras
    ovp=rg+ov  #sueldo con horas extras
    print('Your pay is ',ovp)
else:
    print('Regular') 
    py=fh*fr #pago regular
    print('Your pay is ',py)
