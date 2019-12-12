#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

##STEPS

# 1) Implement a function `eating_cookies` that counts the number of possible ways
# #  Cookie Monster can eat all of the cookies in the jar.
# 2) Cookie Monster can eat either 0, 1, 2, or 3 cookies at a time.

## you'll probably want to use recursion for this.
##  How many ways are there to eat 0 cookies? What about a negative number of cookies?
## [0,1,2,3]
## [1,1,2,4]
'''
# without cache, produces 31 ways to eat 5 cookies
def eating_cookies(n):
  if n <= 0:
    return 1
  ## base case

  return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
  ## recursion as well as rule
print(eating_cookies(5))
'''

## with cache, produces 13 ways to eat 5 cookies
def eating_cookies(n, cache={0:0, 0:1, 1:1, 2:2, 3:4}):
  if n in cache:
    return cache[n]
  else:
    cache[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
  return cache[n]
print(eating_cookies(5))


if __name__ == "__main__":
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))


##objects = hashmaps