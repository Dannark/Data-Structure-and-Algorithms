# -*- coding: utf-8 -*-

class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None


def isValidBST(node):
  return _isValidBSTHelper(node, float("-inf"), float("inf"))

def _isValidBSTHelper(n, low, high):
  if n == None:
    return True
  if ((n.val > low and n.val < high)
    and _isValidBSTHelper(n.left, low, n.val)
    and _isValidBSTHelper(n.right, n.val, high)):
    return True
    
  return False

#   5
#  / \
# 4   7
# n = Node(5)
# n.left = Node(4)
# n.right = Node(7)
#print(isValidBST(n))

#   5
#  / \
# 4   7
#    /
#   2
n = Node(5)
n.left = Node(4)
n.right = Node(7)
n.right.left = Node(2)
n.right.left.right = Node(3)
#print(isValidBST(n))