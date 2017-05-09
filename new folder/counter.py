'''Write a program that counts for the user. Let the user enter the starting number,
   the ending number and the amount by which to count'''


print("Enter Starting number: ")                            # Tell the user to input the first number
start = input()                                             # Take input from the user and store it in a variable called first

print("Enter Finishing number: ")                           # Tell the user to input the last number
finish = input()                                            # Take input from the user and store it in a variable called finish

print("increment by: ")                                     # Tell the user to inpput how much will be skippe
increment = input()                                         # Take input from the user and store it in a variable called increment

for x in range(int(start), int(finish), int(increment)):    # Loop through the users input
    print(x)                                                # Print the users requests by counnting the numbers