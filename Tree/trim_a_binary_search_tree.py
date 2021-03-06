# -*- coding: utf-8 -*-
"""Trim a Binary Search Tree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_53gcldq8zw7-gyriWvzX-cNDvpNZCku
"""

class Node(object):
  def __init__(self, val=None, parent=None):
    self.left = None
    self.right = None
    self.parent = parent
    self.val = val

  def leftChild(self, n):
    self.left = n
    n.parent = self
  
  def rightChild(self, n):
    self.right = n
    n.parent = self

def TrimBST(tree, min, max):
  minNode = findNodeVal(tree, min)

  minNode.left = None
  if minNode.parent.parent.left == minNode.parent:
    minNode.parent.parent.leftChild(minNode)
  else:
    minNode.parent.parent.rightChild(minNode)

  maxNode = findNodeVal(tree, max)
  maxNode.right = None
  if maxNode.parent.parent.left == maxNode.parent:
    maxNode.parent.parent.leftChild(maxNode)
  else:
    maxNode.parent.parent.rightChild(maxNode)
  traverse(r)

  return

def findNodeVal(tree, min, lowest=None):
  currentNode = tree
  if not currentNode:
    return lowest
  
  if currentNode.val >= min:
    lowest = findLowestVal(currentNode.left, min, currentNode)
  else:
    lowest = findLowestVal(currentNode.right, min, lowest)
  return lowest

r = Node(8)
r.leftChild(Node(3))
r.left.leftChild(Node(1))
r.left.rightChild(Node(6))
r.left.right.leftChild(Node(4))
r.left.right.rightChild(Node(7))

r.right = Node(10)
r.right.rightChild(Node(14))
r.right.right.leftChild(Node(13))

TrimBST(r, 5, 13)

# A Better SOLUTION
class Node(object):
  def __init__(self, val=None):
    self.left = None
    self.right = None
    self.val = val

def trimBST(tree, min, max):
  if not tree:
    return

  tree.left = trimBST(tree.left, min, max)
  tree.right = trimBST(tree.right, min, max)

  if min <= tree.val <= max:
    return tree
  
  if tree.val < min:
    return tree.right

  if tree.val > max:
    return tree.left
  pass

r = Node(8)
r.left = Node(3)
r.left.left = Node(1)
r.left.right = Node(6)
r.left.right.left = Node(4)
r.left.right.right = Node(7)

r.right = Node(10)
r.right.right = Node(14)
r.right.right.left = Node(13)

traverse(trimBST(r, 5, 13))

"""## Visualize Data"""

def traverse(n):
  next = n
  nodes = [next]
  currentCount = 1
  nextCount = 0
  while len(nodes) != 0:
    
    currentNode = nodes.pop(0)
    print(currentNode.val, end = ' ')
    currentCount -= 1

    if currentNode.left:
      nodes.append(currentNode.left)
      nextCount += 1

    if currentNode.right:
      nodes.append(currentNode.right)
      nextCount += 1

    if currentCount == 0:
      currentCount = nextCount
      nextCount = 0
      print()

traverse(r)