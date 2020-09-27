# -*- coding: utf-8 -*-
"""Unique Character in a String.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZPu6zouU1YJBaMP8eM1-rHqlfe0ur12C
"""

# O(n) Solution
def uni_char(s):

  map = {}

  for n in s:
    if n not in map:
      map[n] = 1
    else:
      return False
  
  return True

uni_char('abcde')

# another Solution using Sets
def uni_char(s):
  return len(set(s)) == len(s)
uni_char('abcdee')

"""
RUN THIS CELL TO TEST YOUR CODE>
"""
from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')
        
# Run Tests
t = TestUnique()
t.test(uni_char)