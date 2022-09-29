han = open('/media/Docs/Cursos/Python/Python_Scrips/FreeCodeCamp/Test_src/mbox-short.txt')
for line in han:
    line = line.strip() #quita espacios del principi y final
    wds=line.split()
 #   print('line:  ',line)
 #  if len(line) <3 or wds[0] != 'From':
    if len(line) <3: #guardia o == '':
        continue #con este parte se evita la parte de en caso de que la linea este vacia no explote el script
    if wds[0] != 'From':
        continue #skip y tales
    print(wds[2])

    #el guardia siempre va de primero antes que la razon del condicional