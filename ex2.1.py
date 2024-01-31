import sys

# The code has a variable “number” which takes in the second element of sys.argv. 
# Sys.argv is a list containing the filename as the first element, followed by a sequence of arguments you type in the command line. 
# This program will take in a number, and determine whether or not it is prime. If it is prime, it will print yes, and if not, it will print no. 
# So there must be a number after "python ./ex2p2.py" ex. "python ./ex2p2.py 42" will print out No
def do_stuff():
    number = int(sys.argv[1])
    if number < 2:
        print('No')
    else:
        for i in range(2, number):
            if number % i == 0:
                print('No')
                return
        print('Yes') #The error is that on line 15, there is only one quotation mark paired with a non quotation mark. 

# Test the function
do_stuff()
