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

        #insert node at appropriate place in tree
        while(True):
            current = self.changeColors(current)#Flip Colors on condition
            if(data < current.data):#is left branch
                if hasattr(current,'leftChild'):#Check that node has leftChild
                    current = current.leftChild
                else:#create that node
                    current.leftChild = self.Node(data)
                    self.validateColors(current)#checks rule3
                    break
            if(data > current.data):#Is right branch
                if hasattr(current,'rightChild'):#Check that node has rightChild
                    current = current.rightChild
                else:#create that node
                    current.rightChild = self.Node(data)
                    current = current.rightChild#X
                    self.validateColors(current)#checks rule3
                    break
        self.balanceTree(data)

    def balanceTree(self,data):
        """balance the tree so red-red rules are not violated and tree height rules are not violated
        """
        Ptree = self.findP(data)
        if Ptree.rb == False:#pg450 possibility 1
            return #The tree is already balanced
        GPtree = self.findGP(data)
        nodeOutside = ((lastDir == 'left' and current.data == parent.leftChild) or (lastDir == 'right' and current.data == parent.rightChild))
        nodeInside = ((lastDir == 'right' and current.data == parent.leftChild) or (lastDir == 'left' and current.data == parent.rightChild))
        if self.findSubTreeRoot(data).rb == True and nodeOutside:
            #Do possibility 2 actions
            GPtree.rb = not GPtree.rb
            Ptree.rb = not Ptree.rb
            #Perform grandparent rotation
            if ():
            self.rotate(rdir,GPtree.data)
        if self.fundSubTreeRoot(data).rb == True and nodeInside:
            #Do Possibility 3 actions

                #Post Insertion Rotations
        
        # if parent.rb == False:#If parent is black, no insertion issue
        #     True == True#do Nothing
        # elif parent.rb == True and nodeOutside:#parent is red and X is outside
        #     grandparent.rb = not grandparent.rb#pg 451 data struct switch color of X's grandparent
        #     parent.rb= not parent.rb#pg 451 data struct switch color of X's parent
        #     #will need a rotation right or rotation left, whichever raises X
        #     if(lastDir == 'left'):#If outside on left branch, rotate cw
        #         self.root = self.rotateGP('cw',grandparent.data)

        # elif parent.rb == True and nodeInside:#parent is red and X is inside


    def findGP(self,num):
        """Returns the GrandParent of node with node.data = num
        """
        current = self.root
        while(True):
            try:
                grandparent = parent
            except:
                pass
            parent = current#Parent
            if(num < current.data):
                current = current.leftChild
            elif(num > current.data):
                current = current.rightChild
            else:#data = num
                return grandparent

    def findP(self,num):
        """Find Parent of node with num
        """
        current = self.root
        while(True):
            parent = current#Parent
            if(num < current.data):
                current = current.leftChild
            elif(num > current.data):
                current = current.rightChild
            else:#data = num
                return parent

    def rotateGP(self,dir,GPnum):
        """Rotate branch by direction dir with top at GPnum
        """
        current = self.findSubTreeRoot(GPnum)
        if dir == cw:
            #Push down right side
        else:#dir == 'ccw'
            #Push down left side

    def findSubTreeRoot(self,num):
        """
        Returns: Tree with root at num
        """
        current = self.root
        while(True):
            if(num < current.data):
                current = current.leftChild
            elif(num > current.data):
                current = current.rightChild
            else:#data = num
                return current

    def validateColors(self,current):
        """Check for red red violations
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
