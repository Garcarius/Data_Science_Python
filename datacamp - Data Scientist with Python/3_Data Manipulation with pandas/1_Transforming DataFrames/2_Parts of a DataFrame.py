""" To better understand DataFrame objects, it's useful to know that they consist of three components, stored as attributes:

.values: A two-dimensional NumPy array of values.
.columns: An index of columns: the column names.
.index: An index for the rows: either row numbers or row names.
You can usually think of indexes as a list of strings or numbers, though the pandas Index data type allows for more sophisticated options. (These will be covered later in the course.)

homelessness is available. """

import pandas as pd
path=r'/media/documentos/Cursos/Data Science/Python/Data_Science_Python/data_sets/'
file='homelessness.csv'
homelessness=pd.read_csv(path+file,index_col=0)
print(homelessness.values)
print(homelessness.columns)
print(homelessness.index)
