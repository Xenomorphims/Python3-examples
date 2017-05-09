four = 4
nine = 9

# the 'and' operator checks whether both conditions
# are True and then prints out the statement
if four > nine > four:
    print('The number is between 4 and 10')
else:
    print('No number in between')

# the 'or' operator checks if one of the conditions
# are True and then prints out the statement
if four > nine or four < nine:
    print('The number is between 4 and 10')
