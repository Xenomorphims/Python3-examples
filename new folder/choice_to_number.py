def choice_to_number(choice):
	if choice == 'Usain':
		print('1')
	if choice == 'Me':
		print('2')
	if choice == 'Qazi':
		print('3')
		
	return choice
	
print(choice_to_number('Me'))

def test_choice_to_number():
	assert choice_to_number('Usain') == 1
	assert choice_to_number('Me') == 2
	assert choice_to_number('Qazi') == 3
	
def test_all():
	try:
		test_choice_to_number()
		#test_choice_to_choice()
	
	except AssertionError:
		import wrong
		
	else:
		import success
		
	test_all()
	
	
	
	
	
	
	
	
	
	
	
	
	