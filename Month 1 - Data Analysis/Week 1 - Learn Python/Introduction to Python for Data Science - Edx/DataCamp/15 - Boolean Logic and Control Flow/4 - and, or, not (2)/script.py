
'''
Exercise :
    To see if you completely understood the boolean operators, have a look at the following piece of Python code:

    x = 8
    y = 9
    not(not(x < 3) and not(y > 14 or y > 10))

----------------------------------------------------------------------------   
Questions: 
    What will the result be if you exectue these three commands in the IPython Shell?

NB: Notice that not has a higher priority than and and or, it is executed first.

Answer : False

'''

x = 8
y = 9
print(not(not(x < 3) and not(y > 14 or y > 10)))

