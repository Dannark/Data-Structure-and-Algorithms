# -*- coding: utf-8 -*-
"""Linked List Implementation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fdVxvaxf9jJow4g9vsvlUqBVHWhy9WKP
"""

# Singly Linked List
class Node(object):
  def __init__(self, value):
    self.value = value
    self.nextnode = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print(b.nextnode.value)

# Doubly Linked List
class Node(object):
  def __init__(self, value):
    self.value = value
    self.nextnode = None
    self.prevnode = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

b.prevnode = a
c.prevnode = b
d.prevnode = c

print(b.prevnode.value)