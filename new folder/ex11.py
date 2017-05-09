print('How old are you?')
age = int(input(': '))
if age < 17:
    print('You are still a child')
else:
    print('You are all grown up')
print('How tall are you?')
height = int(input(': '))
print('How much do you weight?')
weight = int(input(': '))

print("So, you're %r old, %r tall and %rheavy." % (
    age, height, weight))
