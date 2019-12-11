#!/usr/bin/python

import argparse
#STEPS
#1) function `find_max_profit` that receives as input a list of stock prices.

#2) You must buy first before selling;

#3) Your function should return the maximum profit

def find_max_profit(prices):
  current_min_price_so_far = prices[0]
  ##day we buy
  ## setting up current min as 0 index of prices list

  max_profit_so_far = prices[1]- current_min_price_so_far
  ## day we sell
  ## max profits for now is the 1st index of prices minutes current_min

  for price in prices[1: len(prices)-1]:
  ## for a single price in prices list starting after the  first item in prices until last

    if (price - current_min_price_so_far) > max_profit_so_far:
    ## if the price -  current min is greater than max profits

            max_profit_so_far = price - current_min_price_so_far
            #  max profits will be equal to price - current min

    if price < current_min_price_so_far:
    ## if the price is less than the current min

            current_min_price_so_far = price
            ##current min will now be = to price
  return max_profit_so_far

p = [1050, 270, 1540, 3800, 2]
print(find_max_profit(p))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))