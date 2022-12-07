""" loc and iloc (3)
It's also possible to select only columns with loc and iloc. In both cases, you simply put a slice going from beginning to end in front of the comma: """

import pandas as pd
path=r'//media//documentos//Cursos//Python//Python_Scrips//FreeCodeCamp//data_sets//'
cars=pd.read_csv(path+ 'cars.csv',index_col=0)

cars.loc[:, 'country']
cars.iloc[:, 1]

cars.loc[:, ['country','drives_right']]
cars.iloc[:, [1, 2]]

""" 
Print out the drives_right column as a Series using loc or iloc.
Print out the drives_right column as a DataFrame using loc or iloc.
Print out both the cars_per_cap and drives_right column as a DataFrame using loc or iloc. 
"""
# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap','drives_right']])



