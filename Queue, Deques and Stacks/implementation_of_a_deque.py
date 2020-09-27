# -*- coding: utf-8 -*-
"""Implementation of a Deque.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s7HQDyGDOPEPxF9HR0LbkbgQsB8zTdmm
"""

class Deque(object):
  def __init__(self):
    self.items = []

  def addFront(self, item):
    self.items.insert(0, item)
  
  def addBack(self, item):
    self.items.append(item)

  def isEmpty(self):
    return self.items == []

  def removeFront(self):
    return self.items.pop()
  
  def removeBack(self):
    return self.items.pop(0)

  def size(self):
    return len(self.items)

s = Deque()
s.addFront('one')
s.addFront('two')

s.addBack(1)
s.addBack(2)

print(s.items)

s.removeBack()
print(s.items)

s.removeFront()
print(s.items)