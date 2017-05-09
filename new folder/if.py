number = 23
guess = int(input('Enter an integer: '))

if guess == number:
    #New block starts here
    print ('Congratulations, you guessed it!')
    print ('(But you do not win any prizes! XD)')
    #New block ends here
elif guess < number:
    #Another block
    print ('No, it is a little higher than that.')
    #You can do whatever you want in this block...
else:
    print('No, it is a little lower than that.')
    #You must have guessed > number to rech here...

print ('Done')
#This last statement is always executed...
#after the 'if' statement is executed...
