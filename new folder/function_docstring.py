def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be intergers.'''
    #Convert to interger, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is minimum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)
