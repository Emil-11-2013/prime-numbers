# Pogram to check if given number is prime or not

from math import sqrt
number = int(input("Enter your number "))


# If given number is greater than 1
if (number > 1):


    # Check if number is divisable by 2 to number/2
    for i in range(2, int(sqrt(number))+1):


        # If divisable by any number it is non prime number
        if (number % i) == 0:
            print(number, "is not a prime number")
            break

        else:
            print(number, "is a prime number")

else:
    print(number, "is not a prime number")    