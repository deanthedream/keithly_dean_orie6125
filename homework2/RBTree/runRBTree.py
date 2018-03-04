import RBTree


data = 50 #the first node of the tree
tree = RBTree.Tree(data)
tree.insert(50)
tree.insert(40)
tree.insert(20)
print(tree.root.rightChild.data)
print(tree.root.leftChild.data)
#print(dir(tree))
#print(tree.root.data)


print(saltyburrito)
#tree.insert(data)
