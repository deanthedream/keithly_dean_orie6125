import RBTree


data = 50 #the first node of the tree
tree = RBTree.Tree(data)
tree.insert(2)
tree.insert(60)
tree.insert(70)
print(tree.root.rightChild.data)
print(tree.root.leftChild.data)
#print(dir(tree))
#print(tree.root.data)


print(saltyburrito)
#tree.insert(data)
