Path='/media/Docs/Cursos/Python/Python_Scrips/FreeCodeCamp/Test_src/'
file_n='mbox-short.txt'
fullfile=Path+file_n
fh=open(fullfile) #solo es un handler
for lx in fh: #para poder leer debes usar un ciclo que vaya linea por linea
    ly=lx.strip() #quitar espacios
    print (ly.upper()) #para colocarlo en mayusculas