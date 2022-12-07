""" loc and iloc (2)
loc and iloc also allow you to select both rows and columns from a DataFrame. To experiment, try out the following commands in the IPython Shell. Again, paired commands produce the same result. """

import pandas as pd
path=r'//media//documentos//Cursos//Python//Python_Scrips//FreeCodeCamp//data_sets//'
cars=pd.read_csv(path+ 'cars.csv',index_col=0)

cars.loc['IN', 'cars_per_cap']
cars.iloc[3, 0]

cars.loc[['IN', 'RU'], 'cars_per_cap']
cars.iloc[[3, 4], 0]

cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
cars.iloc[[3, 4], [0, 1]]

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])
print(cars.iloc[5, 2])
# Print sub-DataFrame
print(cars.loc[['MOR','RU'], ['drives_right','country']])