
'''
Exercise:
    With loc you can do practically any data selection operation on DataFrames you can think of. 
    loc is label-based, which means that you have to specify rows and columns based on their row and column labels.

    Try out the following commands in the IPython Shell to experiment with loc to select observations:

        cars.loc['RU']
        cars.loc[['RU']]
        cars.loc[['RU', 'AUS']]
    As before, code is included that imports the cars data as a Pandas DataFrame.

----------------------------------------------------------------------------------------
Instructions:
    - Use loc to select the observation corresponding to Japan as a Series. 
    The label of this row is JAP. Make sure to print the resulting Series.
    - Use loc to select the observations for Australia and Egypt as a DataFrame. 
    You can find out about the labels of these rows by inspecting cars in the IPython Shell. 
    Make sure to print the resulting DataFrame.
'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc['JAP'])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS','EG']])

