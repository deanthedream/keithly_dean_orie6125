from RBTree import Tree, Node, nil


#data = 50 #the first node of the tree
nil_leaf = nil()
tree = Tree(50,nil_leaf)


tree.RB_insert(Node(10,nil_leaf))
tree.RB_insert(Node(20,nil_leaf))
tree.RB_insert(Node(21,nil_leaf))
tree.RB_insert(Node(22,nil_leaf))
tree.RB_insert(Node(23,nil_leaf))

print(tree.root.key)
print(tree.root.right.key)
print(tree.root.left.key)

print(saltyburrito)

##############################
tree = RBTree.Tree(50)
tree.insert(50)
tree.insert(40)
tree.insert(20)
print(tree.root.rightChild.data)
print(tree.root.leftChild.data)
#print(dir(tree))
#print(tree.root.data)


print(saltyburrito)
#tree.insert(data)
