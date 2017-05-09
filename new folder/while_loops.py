# a 'while' loop is basically saying 'as long as'

# we first set the variable 'num' to 9
num = 0

# we then test if 0 is less than or equal to 100
while num <= 100:
    # next we print the variable num which is 0
    print(num)
    # and increment it by 5 (skips five numbers)
    num += 5


# a 'for' loop is basically assigning a variable to a value
# over and over again

# we first create a variable assigned to a list
op = ['windows', 'linux', 'macOS', 'ubuntu']

# we first call the for loop and assign 'i' to all the
# thins in the set
for i in op:
    # we then print out each member of the list separately
    print('One of the best operating systems is', i)
