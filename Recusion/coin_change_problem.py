# -*- coding: utf-8 -*-
"""Coin Change Problem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zv8hr9jp1IY0nStQ32y57PFnAaZXwfMn
"""

# My own implementation, looks like i finally mastered it huh.
target = 63
coins = [1,5,10, 25]

def rec_coin(target, coins):
  return len(rec_coin_helper(target, coins))

def rec_coin_helper(target, coins):
  back_coins = coins[::-1]
  
  # Base Case
  if target == 1:
    return [target]

  for n in back_coins:
    if n <= target:
      c = rec_coin_helper(target - n, coins)
      if c:
        return [n, *c]
      else:
        return [n]

rec_coin(target, coins)

# with memoization implementation
target = 16
coins = [1,5,10]

cache = [None] * (target+1)

def rec_coin(target, coins):
  global cache
  if cache[target] != None:
    print('(loaded from cache)')
    return cache[target]
  cache[target] = len(rec_coin_helper(target, coins))
  return cache[target]

def rec_coin_helper(target, coins):
  back_coins = coins[::-1]
  
  # Base Case
  if target == 1:
    return [target]

  for n in back_coins:
    if n <= target:
      c = rec_coin_helper(target - n, coins)
      if c:
        return [n, *c]
      else:
        return [n]

rec_coin(target, coins)

rec_coin(target, coins)

"""
RUN THIS CELL TO TEST YOUR FUNCTION.
NOTE: NON-DYNAMIC FUNCTIONS WILL TAKE A LONG TIME TO TEST. IF YOU BELIEVE YOU HAVE A SOLUTION
"""

from nose.tools import assert_equal

class TestCoins(object):
    
    def check(self,solution):
        coins = [1,5,10,25]
        assert_equal(solution(45,coins),3)
        assert_equal(solution(23,coins),5)
        assert_equal(solution(74,coins),8)

        print ('Passed all tests.')
        
# Run Test

test = TestCoins()
test.check(rec_coin)