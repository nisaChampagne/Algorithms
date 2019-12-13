#!/usr/bin/python

##STEPS
#1) Write a function`making_change` that
#  receives as input an amount of money in
#  cents as well as an array of coin
# denominations

#2) calculates the total number of ways in which
# change can be made for the input amount
#  using the given coin denominations.

##NOTES
# Since this is a bank, you have an
#  infinite supply of coinange.

# For example, `making_change(10)` should return
#  4, since there are 4 ways to make change for
#  10 cents using pennies, nickels, dimes,
#  quarters, and half-dollars:
'''
1. We can make change for 10 cents using 10 pennies
2. We can use 5 pennies and a nickel
3. We can use 2 nickels
4. We can use a single dime
'''
##ASSUMPTIONS
## amount being less than 5 but greater than 0 will usually return only 1 way
## denom has to have a length greater than 0
## amount over 5 is fair game
## no negative amounts


import sys
def making_change( amount, denominations ):
  if amount < 5 and amount >= 0:
    return 1
  elif amount < 0 or not denominations:
    return 0
  else:
    coin = denominations[-1]
    return making_change(amount - coin,denominations) + making_change(amount, denominations[:-1])
    ## [:1] safe way to remove last character
    ## [-1] getting last number from denominations list

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")

