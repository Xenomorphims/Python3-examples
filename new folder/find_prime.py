# Python program to check if the input number is prime or not

# A prime number (or a prime) is a natural number greater than 1
# that has no positive divisors other than 1 and itself.
# A natural number greater than 1 that is not a prime number is called a composite number.
# For example, 5 is prime because 1 and 5 are its only positive integer factors,
# whereas 6 is composite because it has the divisors 2 and 3 in addition to 1 and 6.


def checkPrimeNumber(num):
 # prime numbers are greater than 1
 if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

 # if input number is less than
 # or equal to 1, it is not prime
 else:
    print(num, "is not a prime number")


# take input from the user
while True:
 num = int(input("Enter a number: "))
 if num!=0:
  checkPrimeNumber(num)
  print ("Enter 0 to Exit \n");

 if num==0:
     print ("------------ Exit -------------")
     break