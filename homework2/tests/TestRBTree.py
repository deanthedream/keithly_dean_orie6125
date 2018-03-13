import unittest
from RBTree import Tree, nil, Node

class TestRBTree(unittest.TestCase):

	nil_leaf= nil()

	def setUp(self):
		pass

	def test_RB_insert(self):
		for j in np.arange(30):#Generate 30 different trees
			val = [np.random.randint(1,1000) for x in np.arange(20)]
			val = np.unique(np.asarray(val))
			tree = Tree(val[0],nil_leaf)
			for i in np.arange(len(val)-1)+1:
				tree.RB_insert(Node(val[i],nil_leaf))
		

		tree.RB_insert(Node(20,nil_leaf))
		tree.RB_insert(Node(21,nil_leaf))
		tree.RB_insert(Node(22,nil_leaf))
		tree.RB_insert(Node(23,nil_leaf))


	def test_RB_insert_fixup(self):

	def test_RB_delete(self):
		tree = Tree(10,nil_leaf)
		tree.RB_insert(Node(10,nil_leaf))
		tree.RB_insert(Node(20,nil_leaf))
		tree.RB_insert(Node(21,nil_leaf))
		tree.RB_insert(Node(22,nil_leaf))
		tree.RB_insert(Node(23,nil_leaf))
		tree.RB_delete()

	def test_print_tree(self):
		#Also tests init_depth_first_search
		tree = Tree(50)


	def test_find_node(self):#DONE #could be randomized
		tree = Tree(50,nil_leaf)
		tree.RB_insert(Node(10,nil_leaf))
		tree.RB_insert(Node(260,nil_leaf))

		x = tree.find_node(50)
		assert(x.key == 50,'Key != 50')

		x = tree.find_node(260)
		assert(x.key == 260,'Key != 260')


# 	def test_root(self):
# 		data = 1
# 		tree = Tree(data)
# 		self.assertEqual(tree.root.rb,False)

# 	def test_insert(self):
# 		data = 40
# 		tree = Tree(data)
# 		tree.insert(10)
# 		self.assertEqual(tree.root.leftChild.data,10)

# 	def test_validateColors(self):
# 		data = 40
# 		tree = Tree(data)
# 		tree.insert(10)
# 		self.assertEqual(tree.root.rb,False)#root is black
# 		#print(tree.root.rb)
# 		#print(tree.root.leftChild.data)
# 		#print(tree.root.leftChild.rb)
# 		self.assertEqual(tree.root.leftChild.rb,True,'2 node tree does not have red left node')#single left node is red

# 		tree.insert(60)
# 		self.assertEqual(tree.root.rb,False)
# 		self.assertEqual(tree.root.rightChild.rb,False)
# 		self.assertEqual(tree.root.leftChild.rb,False)

# 	def test_changeColors(self):
# 		data = 40
# 		tree = Tree(data)
# 		tree.root.rb = False
# 		tree.root.rightChild = tree.Node(60)
# 		tree.root.leftChild = tree.Node(10)
# 		#print(tree.root.rightChild.rb)
# 		#print(tree.root.leftChild.rb)
# 		tree.changeColors(tree.root)
# 		self.assertEqual(tree.root.leftChild.rb,False)
# 		self.assertEqual(tree.root.rightChild.rb,False)


if __name__ == '__main__':
    unittest.main()