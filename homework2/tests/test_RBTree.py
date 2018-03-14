import unittest
from RBTree.RBTree import RBTree
from RBTree.nil import nil
from RBTree.Node import Node
import numpy as np
import random

nil_leaf= nil()#Instantiate the global nil leaf

#Functions touched for certain
#RB_insert
#RB_insert_fixup
#left_rotate
#right_rotate
#RB_insert_fixup
#init_depth_first_search
#depth_first_search
#find_node
#tree_minimum
#print_tree


class test_RBTree(unittest.TestCase):

    

    def setUp(self):
        #Generate Tree Randomly for each case
        val = [np.random.randint(1,1000) for x in np.arange(100)]
        val = np.unique(np.asarray(val))
        tree = RBTree(val[0],nil_leaf)
        for i in np.arange(len(val)-1)+1:
            tree.RB_insert(Node(val[i],nil_leaf))
        self.tree = tree
        self.val = val
        pass

    def test_RB_insert(self):
        """Randomly generate 30 trees from scratch to ensure all insert and fixup functions are tested
        """
        for j in np.arange(100):#Generate 30 different trees
            val = [np.random.randint(1,1000) for x in np.arange(100)]#generate 100 random integers between 1 and 1000
            val = np.unique(np.asarray(val))#ensure all integers are unique
            tree = RBTree(val[0],nil_leaf)#create tree with first val
            for i in np.arange(len(val)-1)+1:#Iterate through remaining val
                tree.RB_insert(Node(val[i],nil_leaf))#insert each val

    def test_RB_delete(self):
        #tree = self.tree
        #val = self.val
        for asdfk in np.arange(10):#create and delete tree 10 times
            val = [np.random.randint(1,1000) for x in np.arange(100)]#generate array of random numbers
            val = np.unique(np.asarray(val))#remove all duplicates
            random.shuffle(val)#randomize the val array
            tree = RBTree(val[0],nil_leaf)#val_leaf
            for i in np.arange(len(val)-1)+1:
                tree.RB_insert(Node(val[i],nil_leaf))

            myLen = len(val)
            for i in np.arange(myLen-1):#delete 100 targets
                tree.RB_delete(tree.find_node(val[0]))#delete action
                #print(len(val))
                tmp = val == val[0]
                tmp = [not i for i in tmp]
                val = val[tmp]
        # tree = RBTree(50,nil_leaf)
        # tree.RB_insert(Node(10,nil_leaf))
        # tree.RB_insert(Node(20,nil_leaf))
        # tree.RB_insert(Node(21,nil_leaf))
        # tree.RB_insert(Node(22,nil_leaf))
        # tree.RB_insert(Node(23,nil_leaf))
        # tree.RB_delete(tree.find_node(10))
        # tree.RB_delete(tree.find_node(20))
        # tree.RB_delete(tree.find_node(21))

    def test_find_node(self):#DONE #could be randomized
        tree = RBTree(50,nil_leaf)
        tree.RB_insert(Node(10,nil_leaf))
        tree.RB_insert(Node(260,nil_leaf))

        x = tree.find_node(50)
        self.assertTrue(x.key == 50,'Key != 50')

        x = tree.find_node(260)
        self.assertTrue(x.key == 260,'Key != 260')

    def test_init_depth_first_search(self):
        tree = self.tree
        val = self.val

        tree.init_depth_first_search()

    def test_runRBTree(self):
        from RBTree import runRBTree

    def test_print_tree(self):
        tree = self.tree
        val = self.val

        tree.print_tree()

    def test_tree_minimum(self):
        tree = self.tree
        val = self.val

        tree.tree_minimum(tree.root)


if __name__ == '__main__':
    unittest.main()