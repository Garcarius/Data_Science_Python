#'CIBFont Sans Light'
#Pt(11)
# RGBColor(0x59, 0x59, 0x59)
#WD_PARAGRAPH_ALIGNMENT.JUSTIFY
import pandas as pd
from docxtpl import DocxTemplate
import time
import random

src='/media/documentos/Cursos/Python/Test/Cartas/'
pl='lista.xlsx'
dtpl='carta_test.docx'
df=pd.read_excel(src+pl)
print(df,'\n')

print(df.iloc[[0]])


def mkw(n):
    tpl = DocxTemplate(src+dtpl) # In  directory
    df = pd.read_excel(src+pl)
    df_to_doct = df.to_dict() # dataframe -> dict for the template render
    context = df.to_dict(orient='records')
    tpl.render(context[n])
    tpl.save(src+"Carta_Aprobación_"+str(df["id"].iloc[n])+"_"+str(df["proyecto"].iloc[n]) +".docx" )
    print("Carta_Aprobación_"+str(df["id"].iloc[n])+"_"+str(df["proyecto"].iloc[n]) +".docx \n")
    # Wait a random time - increase to (60,180) for real production run.
    wait = time.sleep(random.randint(1,2))

#-------------------Main---------------------#  

df2 = len(pd.read_excel(src+pl)) 
print ("There will be ", df2, "files")

for i in range(0,df2):
    print("Making file: ",f"{i}," ,"..Please Wait...\n")
    mkw(i)
    
    
print("Done! - Now check your files")