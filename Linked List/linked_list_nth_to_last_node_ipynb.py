# -*- coding: utf-8 -*-
"""Linked List Nth to Last Node .ipynb.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cr1A4QVH-0fzpToybYwX4udKRlzkGqF-
"""

# Write a function that takes a head node and an integer value n and then returns the nth to last node in the linked list. For example, given:
class Node:
  def __init__(self, value):
    self.value = value
    self.nextnode  = None

# bad implementation
def nth_to_last_node(n, head):
  next = head
  last_nth = []

  while next:
    if len(last_nth) >= n:
      last_nth.pop(0)
    
    last_nth += [next]
    next = next.nextnode

  return last_nth[0]

# Better solution
def nth_to_last_node(n, head):
  left_pointer = head
  right_pointer = head

  for i in range(n-1):
    if not right_pointer.nextnode:
      raise LookupError('Error: n is larger than Linked List')
    right_pointer = right_pointer.nextnode

  while right_pointer.nextnode:
    left_pointer = left_pointer.nextnode
    right_pointer = right_pointer.nextnode
  return left_pointer

#test
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(2, a)
target_node.value