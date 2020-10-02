# -*- coding: utf-8 -*-

class BinaryTree(object):
  def __init__(self, value):
    self.key = value
    self.leftNode = None
    self.rightNode = None

  def insertLeft(self, value):
    if self.leftNode == None:
      self.leftNode = BinaryTree(value)
    else:
      t = BinaryTree(value)
      t.leftChild = self.leftNode
      self.leftNode = t

  def insertRight(self, value):
    if self.rightNode == None:
      self.rightNode = BinaryTree(value)
    else:
      t = BinaryTree(value)
      t.rightChild = self.rightNode
      self.rightNode = t

  def getLeftChild(self):
    return self.leftNode

  def getRightChild(self):
    return self.rightNode
  
  def setRootVal(self, obj):
    self.key = obj

  def getRootVal(self):
    return self.key


def preorder(tree):
  if tree != None:
    print(tree.getRootVal())
    preorder(tree.getLeftChild())
    preorder(tree.getRightChild())

# b = BinaryTree('a')
# b.insertLeft('b')
# b.insertLeft('c')
# b.insertLeft('d')
# b.insertRight('e')
# b.insertRight('f')

#preorder(b)