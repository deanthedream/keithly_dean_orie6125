from RBTree import RBTree
from RBTree import nil
from RBTree import Node
import numpy as np


#data = 50 #the first node of the tree
nil_leaf = nil()
tree = RBTree(50,nil_leaf)


tree.RB_insert(Node(10,nil_leaf))
tree.RB_insert(Node(20,nil_leaf))
tree.RB_insert(Node(21,nil_leaf))
tree.RB_insert(Node(22,nil_leaf))
tree.RB_insert(Node(23,nil_leaf))

print(tree.root.key)
print(tree.root.right.key)
print(tree.root.left.key)

tree.init_depth_first_search()
print(tree.myArray)

