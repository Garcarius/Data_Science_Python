""" Cars per capita (2)
Remember about np.logical_and(), np.logical_or() and np.logical_not(), the NumPy variants of the and, or and not operators? You can also use them on Pandas Series to do more advanced filtering operations.

Take this example that selects the observations that have a cars_per_cap between 10 and 80. Try out these lines of code step by step to see what's happening.

cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 10, cpc < 80)
medium = cars[between]

Use the code sample provided to create a DataFrame medium, that includes all the observations of cars that have a cars_per_cap between 100 and 500.
Print out medium. """

import pandas as pd
import numpy as np

path=r'/media/documentos/Cursos/Python/Python_Scrips/FreeCodeCamp/data_sets/'
file='cars.csv'
cars=pd.read_csv(path+file,index_col=0)

cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

print(medium)