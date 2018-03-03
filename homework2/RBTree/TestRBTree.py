import unittest
from RBTree import Tree

class TestRBTree(unittest.TestCase):

	def setUp(self):
		pass

	def test_root(self):
		data = 1
		tree = Tree(data)
		self.assertEqual(tree.root.rb,False)

	def test_insert(self):
		data = 40
		tree = Tree(data)
		tree.insert(10)
		self.assertEqual(tree.root.leftChild.data,10)

	def test_validateColors(self):
		data = 40
		tree = Tree(data)
		tree.insert(10)
		self.assertEqual(tree.root.rb,False)#root is black
		#print(tree.root.rb)
		#print(tree.root.leftChild.data)
		#print(tree.root.leftChild.rb)
		self.assertEqual(tree.root.leftChild.rb,True,'2 node tree does not have red left node')#single left node is red

		tree.insert(60)
		self.assertEqual(tree.root.rb,False)
		self.assertEqual(tree.root.rightChild.rb,False)
		self.assertEqual(tree.root.leftChild.rb,False)

	def test_changeColors(self):
		data = 40
		tree = Tree(data)
		tree.root.rb = False
		tree.root.rightChild = tree.Node(60)
		tree.root.leftChild = tree.Node(10)
		#print(tree.root.rightChild.rb)
		#print(tree.root.leftChild.rb)
		tree.changeColors(tree.root)
		self.assertEqual(tree.root.leftChild.rb,False)
		self.assertEqual(tree.root.rightChild.rb,False)


if __name__ == '__main__':
    unittest.main()