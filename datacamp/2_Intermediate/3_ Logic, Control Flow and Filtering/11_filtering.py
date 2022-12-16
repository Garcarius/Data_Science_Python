import pandas as pd

path=r'/media/documentos/Cursos/Python/Python_Scrips/FreeCodeCamp/data_sets/'
file='brics.csv'

brics=pd.read_csv(path+file,index_col=0)

print(brics[brics ['area'] > 8])