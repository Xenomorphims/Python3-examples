# print([0, 1, 2, 4])
# range(0, 2) --->[0, 1, 2]


# print numbers from 20 to 41 (excluding 40)
for number in range(20, 41):
	print(number)
	
# [1, 2, 3] ---> 6
count = 0
for number in range(1, 4):
	# new_count = old_count + number
	count = count + number
	
# It should be, in this case 6 
# print(count)

# write a function that sums all elements of a
# list and returns them
def sum_list(my_list):
	count = 0
	for number in my_list:
			count = count + number
			
	return count
	
assert sum_list([1, 2, 3]) == 6
assert sum_list([1, 2, 3, 4]) == 10
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	