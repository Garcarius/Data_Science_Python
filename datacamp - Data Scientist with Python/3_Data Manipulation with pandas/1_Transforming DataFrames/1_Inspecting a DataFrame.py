""" Inspecting a DataFrame
When you get a new DataFrame to work with, the first thing you need to do is explore it and see what it contains. There are several useful methods and attributes for this.

.head() returns the first few rows (the “head” of the DataFrame).
.info() shows information on each of the columns, such as the data type and number of missing values.
.shape returns the number of rows and columns of the DataFrame.
.describe() calculates a few summary statistics for each column.

homelessness is a DataFrame containing estimates of homelessness in each U.S. state in 2018. The individual column is the number of homeless individuals not part of a family with children. The family_members column is the number of homeless individuals part of a family with children. The state_pop column is the state's total population.

pandas is imported for you 

Print the head of the homelessness DataFrame.
"""
import pandas as pd
path=r'/media/documentos/Cursos/Data Science/Python/Data_Science_Python/data_sets/'
file='homelessness.csv'
homelessness=pd.read_csv(path+file,index_col=0)

print(homelessness.head(10),'\n')
print(homelessness.info(),'\n')
print(homelessness.shape,'\n')
print(homelessness.describe(),'\n')