import pandas as pd

xpath='/media/documentos/Cursos/Python/Python_Scrips/FreeCodeCamp/Test_src/'
file='Test.xlsx'
xfile=xpath+file

fex=pd.ExcelFile(xfile)

print(fex.sheet_names)

df_test=(fex.parse('Sheet1'))

print(df_test)
