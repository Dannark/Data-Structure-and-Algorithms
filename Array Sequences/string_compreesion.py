# -*- coding: utf-8 -*-
"""String compreesion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_yK0-aOjqkWQzchBqfPhylYIcDk_5rXa
"""

def compress(s):

  letters = ''
  length = len(s);
  i = 0

  while i < length:
    current_letter = s[i]
    amount = 1
    i +=1

    while i < length and current_letter == s[i]:
      i +=1
      amount += 1
    letters += current_letter+str(amount)
  return letters

compress('AABBBBccccCCDeee')

# better version
def compress2(s):  
  length = len(s)
  
  #checks edge cases
  if length == 0:
    return ""
  
  if length == 1:
    return s+"1"

  r = ''
  cnt = 1
  i = 1

  while i < length:

    if s[i] == s[i-1]:
      cnt += 1
    else:
      r += s[i-1] +str(cnt)
      cnt = 1
    i+= 1

  r += s[i-1] + str(cnt)
  return r

compress2('AABccCCC')

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)