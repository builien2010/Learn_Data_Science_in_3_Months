print(np.array(columns).dtypes)
'''
Exercise:
    In this lab, you'll explore a dataset containing information on a university's recent graduates for each department. 
    The URL this dataset can be downloaded from is stored in a variable called recent_grads_url. 
    In this exercise, you'll read in this data using Python's pandas module

----------------------------------------------------------------------------------------
Instructions:
    - Import pandas as pd.
    - Read in the data from recent_grads_url (which is a CSV file) and assign it to a variable called recent_grads.
    - Print the shape of recent_grads.
'''

# Import pandas 
import pandas as pd

# Use pandas to read in recent_grads_url
recent_grads = pd.read_csv('recent_grads_url.csv')

# Print the shape
print(recent_grads.shape)