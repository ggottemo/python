#!python 3
#budget.py - a program to check the budget based current guidelines

M_DECK = .6
DEFAULT = .8

#Command line arguments, must have 2:

import sys, pyperclip

if len(sys.argv) != 2 and len(sys.argv) != 3:
    #checks for exactly two arguments
    print('Usage: python budget.py [price] - price of unit [y/n] - Optional arg for M Deck')
    sys.exit()
try:
    price = float(sys.argv[1]) #select price from command line
    if len(sys.argv) == 2:
        print('Is the unit in M-Deck? (y/n)')
        response = input()
    else:
        if sys.argv[2].lower() != 'y' and sys.argv[2].lower() != 'n':
            print('Invalid Argument: Only enter y or n as a second argument')
            sys.exit()
        response = sys.argv[2]
    if(response.lower() == 'y'):
        pyperclip.copy(price * M_DECK)
        print('Remaining budget of ${:,.2f} has been copied to clipboard'.format(price*M_DECK))
    else:
        pyperclip.copy(price * DEFAULT)
        print('Remaining budget of ${:,.2f} has been copied to clipboard'.format(price*DEFAULT))

except ValueError:
    print('Invalid argument: Please enter a number as the first argument and either the letter "y" or "n" as an optional second')
