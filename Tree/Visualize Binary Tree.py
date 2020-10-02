import tkinter
import sys
from binary_seach_tree_check import *

root = tkinter.Tk()
canvas = tkinter.Canvas(root)
canvas.pack()

# for i in range(10):
#     canvas.create_line(50 * i, 0, 50 * i, 400)
#     canvas.create_line(0, 50 * i, 400, 50 * i)
# canvas.create_rectangle(100, 100, 200, 200, fill="blue")
# canvas.create_line(50, 100, 250, 200, fill="red", width=10)

x = 100
y = 0
def preorder(n, x, y):
  if n != None:
    print(n.val, x,y)
    canvas.create_oval(10+x, 10+y,20+x,20+y, fill="blue")

    preorder(n.left, x-25,y+25)
    preorder(n.right, x+25,y+25)

preorder(n,x,y)



    #canvas.create_oval(10, 10,20,20, fill="blue")

root.mainloop()