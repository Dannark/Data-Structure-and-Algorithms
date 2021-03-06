# -*- coding: utf-8 -*-
"""Tree Level Order.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S75hNh7pHJXaZpvoiL7ztrFuuQRWzahr
"""

class Node(object):
  def __init__(self, val=None):
    self.left = None
    self.right = None
    self.val = val

def traverse(n):
  for e in traverse_helper(n).values():
    print(' '.join(e))

def traverse_helper(n, lv = 0, output = {}):
  next = n

  if next:
    if lv not in output:
      output[lv] = [str(n.val)]
    else:
      output[lv] += [str(n.val)]
    
    traverse_helper(next.left, lv+1, output)
    traverse_helper(next.right, lv+1, output)
  return output

r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(4)
r.right.left = Node(5)
r.right.right = Node(6)

traverse(r)

# Better solution
class Node(object):
  def __init__(self, val=None):
    self.left = None
    self.right = None
    self.val = val

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
    

r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(4)
r.right.left = Node(5)
r.right.right = Node(6)

traverse(r)