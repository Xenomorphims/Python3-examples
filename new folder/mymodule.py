def say_hi():
    print('Hi, this is mymodule speaking.')

def intro():
    print('THIS PROGRAM/MODULE WAS\nWRITTEN BY\n\tXENORM')

__version__ = '0.1'

if '__name__' == '__main__':
    print('This module i being run by itself...')
else:
    print('I am being imported from another program')
