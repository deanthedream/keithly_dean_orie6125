#import statements
import numpy as np


#Rule 1. Every Node is Red or Black
#Rule 2. The root is always black
#Rule 3. If a node is red, its children must be black
#Rule 4. Every path from the root to a leaf, or to a null child, 
#           must contain the same number of black nodes

class Tree(object):
    """
    """

    class Node(object):
        """A Node object
        """

        def __init__(self,data):
            self.data = data #data
            self.rb = True#True for Red, Black for False
            #self.leftChild = None
            #self.rightChild = None

    def __init__(self,data):
        """
        """
        self.root = self.Node(data)
        self.root.rb = False#rule1


    def insert(self,data):
        """inserts a node into the tree
        """
        current = self.root
        while(True):
            if(data < current.data):
                if hasattr(current,'leftChild'):#Check that node has leftChild
                    current = current.leftChild
                else:#create that node
                    current.leftChild = self.Node(data)
                    current = self.changeColors(current)#Flip Colors on condtion
                    self.validateColors(current)#checks rule3
                    #balance Tree
                    return
            if(data > current.data):
                if hasattr(current,'rightChild'):#Check that node has rightChild
                    current = current.rightChild
                else:#create that node
                    current.rightChild = self.Node(data)
                    current = self.changeColors(current)#Flip Colors on condition
                    self.validateColors(current)#checks rule3
                    #balance Tree
                    return

    def validateColors(self,current):
        """
        """
        if current.rb == True:#if red
            if hasattr(current.leftChild,'rb'):
                assert(current.leftChild.rb == False,'Red-Red Violation')
            if hasattr(current.rightChild,'rb'):
                assert(current.rightChild.rb == False,'Red-Red Violation')

    def changeColors(self,current):
        """If current node and its left and right children exist, color all black
        """
        if current.rb == False:#the current node is black
            #Check if it has 2 nodes beneath this node
            if hasattr(current,'leftChild') and hasattr(current,'rightChild'):
                #check if both nodes are red
                if current.leftChild.rb == True and current.rightChild.rb == True:
                    current.rb = not current.rb
                    current.leftChild.rb = not current.leftChild.rb#color is now black
                    current.rightChild.rb = not current.rightChild.rb#color is now black

        #Ensure root is black
        if current == self.root:
            current.rb = False

        return current

    def printTree(self):
        """Print Tree
        """

    def delete(self,data):
        """
        """
        #FIND NODE
        #CREATE SUBTREE
        #SAVE SUBTREE
