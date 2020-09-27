# -*- coding: utf-8 -*-
"""Implementation of a Queue.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C1u7vu7JQBCHBKCTf8lmX3bCTub3B-Ee
"""

class Queue(object):
  def __init__(self):
    self.items = []

  def add(self, item):
    self.items.insert(0, item)

  def isEmpty(self):
    return self.items == []

  def pop(self):
    return self.items.pop()

  def size(self):
    return len(self.items)
s = Queue()
s.add('one')
s.add('two')

s.isEmpty()

s.size()