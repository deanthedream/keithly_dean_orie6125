#import statements
import numpy as np

class RBTree(object):
    """A Red Black Tree Implementation
    """

    def __init__(self):
        self.RBTree = list()#initialize RBTree

    def addNumber(self, num):
        """Adds number to red-black tree and modifies tree until a valid tree
        """
        #the number to be added must be unique


        self.RBTree.append({'num':num,'color':'red','leftChild':None,'rightChild':None, 'parent':None})

        #rootIndex = self.findRootIndex()#find root Index of tree
        self.replaceNullTree(num)#we iteratively search the tree until we find a null tree (or phantom leaf) and can insert the element

        while(not self.tree_valid()):
            #We rotate the tree until the tree is valid


    def tree_valid(self):
        """Check if Tree Is Valid

        Return: True or False depending whether the tree is valid or not
        """
        #1 Every Node is Red or Black
        color = np.ones((1,len(self.RBTree)),dtype=bool)#every color starts as True
        for node in np.arange(len(self.RBTree)):
            if not (self.RBTree[node]['color'] == 'red' or self.RBTree[node]['color'] == 'black'):
                color[node] = True #true here indicates there is no color assigned
        assert sum(color) == 0, "All Nodes must have a color"

        #2 The Root Node is Black


        #3 No Red Node has a Red Child

        #4 Every Root to Null Path pass through the same number of Black Nodes

    def findRootIndex(self):
        """Returns the index of the root of the red-black tree
        """
        for index in np.arange(len(self.RBTree)):
            if self.RBTree[index]['parent'] == 'root':
                return index
        print('Error root not found')

    def findIndex(self,num):
        """Returns index of RBTree entry with dict field 'num' of num
        """
        for index in np.arange(len(self.RBTree)):
            if self.RBTree[index]['num'] == num:
                return index
        print('Error num not found')

    def replaceNullTree(self, num):
        """Places the current num of the RBTree entry into the RBTree (determines what its parent is)
        """
        #index = findIndex(num)#this is the index of the current value
        rootIndex = self.findRootIndex()
        index = rootIndex
        while((self.RBTree[index]['leftChild'] != None and self.RBTree[index]['num'] > num) or
            (self.RBTree[index]['rightChild'] != None and self.RBTree[index]['num'] < num)):
            if(self.RBTree[index]['num'] > num):#iteratively check index until at node with 1 empty child
                index = self.findIndex(self.RBTree[index]['rightChild'])#right children are inherently larger
            else:#else num < current index num
                index = self.findIndex(self.RBTree[index]['leftChild'])
        #We now have the index forming the parent of the new Node

        #Populate the Child with the Parent Information
        self.RBTree[index]['parent'] = num

        #Populate Parent with Right Child/Left Child member
        if self.RBTree[index]['num'] > num:#The new node is a leftChild
            self.RBTree[index]['leftChild'] = num
        else:#self.RBTree[index]['num'] > num#The new node is a rightChild
            self.RBTree[index]['rightChild'] = num

    def rotateTree(self):
        #Should be able to rotate trees with a more stable state


