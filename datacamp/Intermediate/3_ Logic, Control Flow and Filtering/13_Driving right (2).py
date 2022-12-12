""" Driving right (2)
The code in the previous example worked fine, but you actually unnecessarily created a new variable dr. You can achieve the same result without this intermediate variable. Put the code that computes dr straight into the square brackets that select observations from cars. """

""" Convert the code to a one-liner that calculates the variable sel as before. """

# Import cars data
import pandas as pd

path=r'/media/documentos/Cursos/Python/Python_Scrips/FreeCodeCamp/data_sets/'
file='cars.csv'
cars=pd.read_csv(path+file,index_col=0)
# Convert code to a one-liner
dr = cars['drives_right']
sel = cars[dr]
# Print sel
print(sel)

print(cars[cars['drives_right']==True])