# -*- coding: utf-8 -*-
"""Find Missing Element.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BdME1Ob2xRbv1_YzE69YWLOqIh9Pq8nB
"""

# This Solution have some problems fo eg, if the numbers are floats that could just lose some critical informations
# of if the arrays are two big, you can get overflow
def finder(arr1, arr2):
    num = 0
    for n in arr1:
        num += n
    
    for n in arr2:
        num -= n
    return num
    pass
  
finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

# best option, not so hard to understand

def finder2(arr1, arr2):
  numbers = {}
  for n in arr1:
    if n not in numbers:
      numbers[n] = 1
    else:
      numbers[n] += 1

  for n in arr2:
    if numbers[n] == 0:
      return n
    else:
      numbers[n] -= 1

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

#This is the cleverest solution but also very hard to understande

def finder3(arr1, arr2):
  result = 0

  for num in arr1+arr2:
    result ^= num
    #print(result)
  return result

finder3([1,2,3,4,5,6,7],[3,7,2,1,4,6])

round((52 / 229) * 100,1)