def is_even(num1, num2):
	return num1 % num2 == 0
	
print(is_even(101, 102))

def test_is_even():
	assert is_even(2, 2) == True
	assert is_even(3, 2) == False
	assert is_even(8, 8) == True
	assert is_even(100, 100) == True
	assert is_even(101, 102) == False
	print("YOUR CODE IS CORRECT!")

test_is_even()	