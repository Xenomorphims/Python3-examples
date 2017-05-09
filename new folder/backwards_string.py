'''Create a program that gets a message from the user 
    and the prints in out backwards'''

'''Pseudocode'''
# get word from user
# create a buffer for backwards string
# loop through each letter, and store it in buffer
# print buffer

# get word from user
user_word = input("\nYour Word: ")

# empty buffer
buffer = ""

# length of user_word
len_word = len(user_word)

# loop through word, store letters in buffer backwards
for i in range(0, len_word):
    letter = user_word(len_word - 1 - i)
    buffer += letter

# see results
print(buffer)
