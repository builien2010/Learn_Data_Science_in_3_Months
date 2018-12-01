
'''
Exercise:
    Now you'll perform some data exploration using the Python pandas module. 
    To get a sense of the data, you'll output statistics such as mean, median, count, and percentiles.

    The DataFrame recent_grads is still in your workspace.

------------------------------------------------------------------------
Instructions:
    - Print the .dtypes of your data so that you know what each column contains.
    - Output basic summary statistics using a single pandas function.
    - With the same function from before, summary statistics for all columns that aren't of type object.

'''

# Print .dtypes
print(recent_grads.dtypes)

# Output summary statistics
print(recent_grads.describe())


# Exclude data of type object
print(recent_grads.describe(exclude=['object']))