import sys
#defining the collatz function.

def collatz(number):
    while True:
        if number == 1:
            sys.exit()
        if number % 2 == 0 :
            number = number // 2
            print(number)
        elif number % 2 == 1:
            number = 3 * number + 1
            print(number)

try:
    number = int(input("Enter a number to see collatz sequence: "))
    collatz(number)
except ValueError:
    print('The input value should be an integer')
