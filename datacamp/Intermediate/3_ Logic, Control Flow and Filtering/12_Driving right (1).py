""" Driving right (1)
Remember that cars dataset, containing the cars per 1000 people (cars_per_cap) and whether people drive right (drives_right) for different countries (country)? The code that imports this data in CSV format into Python as a DataFrame is included in the script.

In the video, you saw a step-by-step approach to filter observations from a DataFrame based on boolean arrays. Let's start simple and try to find all observations in cars where drives_right is True.

drives_right is a boolean column, so you'll have to extract it as a Series and then use this boolean Series to select observations from cars. """

""" Extract the drives_right column as a Pandas Series and store it as dr.
Use dr, a boolean Series, to subset the cars DataFrame. Store the resulting selection in sel.
Print sel, and assert that drives_right is True for all observations. """


import pandas as pd

path=r'/media/documentos/Cursos/Python/Python_Scrips/FreeCodeCamp/data_sets/'
file='cars.csv'

cars=pd.read_csv(path+file,index_col=0)

dr = cars['drives_right']

sel=cars[dr==True]

print(sel)