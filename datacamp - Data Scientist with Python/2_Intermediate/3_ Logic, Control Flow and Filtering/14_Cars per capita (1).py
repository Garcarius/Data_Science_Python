""" Cars per capita (1)
Let's stick to the cars data some more. This time you want to find out which countries have a high cars per capita figure. In other words, in which countries do many people have a car, or maybe multiple cars.

Similar to the previous example, you'll want to build up a boolean Series, that you can then use to subset the cars DataFrame to select certain observations. If you want to do this in a one-liner, that's perfectly fine!

* Select the cars_per_cap column from cars as a Pandas Series and store it as cpc.
* Use cpc in combination with a comparison operator and 500. You want to end up with a boolean Series that's True if the corresponding country has a cars_per_cap of more than 500 and False otherwise. Store this boolean Series as many_cars.
* Use many_cars to subset cars, similar to what you did before. Store the result as car_maniac.
* Print out car_maniac to see if you got it right. """

# Import cars data
import pandas as pd

path=r'/media/documentos/Cursos/Python/Python_Scrips/FreeCodeCamp/data_sets/'
file='cars.csv'
cars=pd.read_csv(path+file,index_col=0)

cpc=cars['cars_per_cap']

many_cars=cpc > 500

print(many_cars)

car_maniac=cars[many_cars]

print(car_maniac)