number = 23
guess = int(input("Enter an interger: "))

if guess == number:
	# New block starts here
	print('Congratulations, you guessed it.')
	print('(But you do not win any prizes)')
	# New block ends here
	
elif guess < number:
	# Another block
	print('No, it is a little higher than that.')
	# You can do whatever you want in this block
	
else:
	print('No, it is a little lower tha that.')
	# You must have guessed > number to reach here
	
print('Done')
# This last statement is always executed, 
# after the if statement is executed.