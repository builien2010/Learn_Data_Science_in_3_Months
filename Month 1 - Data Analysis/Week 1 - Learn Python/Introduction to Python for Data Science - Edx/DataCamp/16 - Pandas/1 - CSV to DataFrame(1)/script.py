'''
Exercise: 
    The DataFrame is one of Pandas' most important data structures. 
    It's basically a way to store tabular data, where you can label the rows and the columns.

    In the exercises that follow, you will be working with vehicle data in different countries. 
    Each observation corresponds to a country, and the columns give information about the number of vehicles per capita,
    whether people drive left or right, and so on. This data is available in a CSV file, named cars.csv. 
    It is available in your current working directory, so the path to the file is simply 'cars.csv'.

    To import CSV data into Python as a Pandas DataFrame, you can use read_csv().
    
-------------------------------------------------------------------------------
Instructions:
    - To import CSV files, you still need the pandas package: import it as pd.
    - Use pd.read_csv() to import cars.csv data as a DataFrame. Store this dataframe as cars.
    - Print out cars. Does everything look OK?

'''
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars =  pd.read_csv('cars.csv')

# Print out cars
print(cars)