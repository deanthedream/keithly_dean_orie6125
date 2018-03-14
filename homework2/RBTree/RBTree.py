#Red Black Tree Datastructure
#Authored by Dean Keithly
from Node import Node
from nil import nil
import numpy as np
import copy

#Rule 1. Every Node is Red or Black
#Rule 2. The root is always black
#Rule 3. If a node is red, its children must be black
#Rule 4. Every path from the root to a leaf, or to a null child, 
#           must contain the same number of black nodes
black = False
red = True
def depth_first_search(tree,x,branchEnum):
    """Recusrive Function to Dive Through Each Root to Branch of Tree Path
    Args: 
        tree - Tree Object with tree.nil leaves
        x - current node in branch
        branchEnum - current boolean array containing left/right movements down branch
    """
    T = tree#redefine tree object for understanding
    branchEnumL = copy.copy(branchEnum)#create a copy of branchEnum for the Left Dive
    branchEnumL.append(0)#append a 0 because moving left
    if x.left == T.nil:#If this is a leaf
        branchEnumL.append('x')#We append a terminator x
        tree.myArray.append(branchEnumL)#We append fully enumerated list of myArray
    else:#we have not reached a leaf
        depth_first_search(tree,x.left,branchEnumL)#recursively call depth_first_search on left branch

    branchEnumR = copy.copy(branchEnum)#create a branch copy for Right Dive
    branchEnumR.append(1)#Append 1 because moving right
    if x.right == T.nil:#if not at terminator
        branchEnumR.append('x')#We append a terminator x
        tree.myArray.append(branchEnumR)#We append fully enumerated list of myArray
    else:#We have not reached a leaf
        depth_first_search(tree,x.right,branchEnum)#recursively call depth_first_search on right branch

    if x.right == T.nil and x.left == T.nil:#Want to print an error if we reach leaves on both
        #print("Root To Leaf")
        return

class RBTree(object):
    def __init__(self,key,nil_leaf):
        """Tree must be initialized with a number
        """
        #Initialize Root and nil
        self.nil = nil_leaf
        self.root = Node(key,nil_leaf)
        self.root.color = black

    def RB_insert(self,z):
        """
        Args:
        z - the Node to insert
        """
        T = self#The Tree
        y = T.nil#parent of current node
        #T.nil is the parent of the current Node
        x = T.root#current node
        while (not (x == T.nil)):#while the current node is not at a leaf
            y=x#update parent holder
            if z.key < x.key:#If the value of node z < value of node x
                x = x.left#move down left branch
            else:#value of node z > value of node x
                x = x.right#move down right branch
        z.p = y#Update node z parent
        if y == T.nil:#If the parent is nil, it is the root node
            T.root = z#Set current node to root
        elif(z.key < y.key):#the node to insert is less than the parent node 
            y.left = z #assign z to be left child of y
        else:
            y.right = z #assign z to be right child of y
        z.left = T.nil#set new node property
        z.right = T.nil#set new node property
        z.color = red#set new node property
        self.RB_insert_fixup(z)# Restore red-black property of tree

    def RB_insert_fixup(self,z):
        """Restores Red Black Correctness of tree
        """
        T = self
        while z.p.color == red: #The color of the current node's parent is red
            if z.p == z.p.p.left:#current node's parent is left child of grandparent
                y = z.p.p.right#set y to right child of grandparent
                if y.color == red:#right child of grandparent is red #CASE 1
                    z.p.color = black#parent color is now black
                    y.color = black#right child of grandparent is black
                    z.p.p.color = red#grandparent is red
                    z = z.p.p#the current node is the grandparent
                else:#right child of grandparent is black
                    if(z == z.p.right):#The current node is an inside child of left branch #CASE 2
                        z = z.p#set current node to parent of current node
                        self.left_rotate(z)#rotate about parent node
                    z.p.color = black#color grandparent node to black #CASE 3
                    z.p.p.color = red#color current grandparent node to red
                    self.right_rotate(z.p.p)#
            else:#same as then clause above but with left and right swapped
                y = z.p.p.left
                if y.color == red: #CASE 4
                    z.p.color = black
                    y.color = black
                    z.p.p.color = red
                    z = z.p.p
                else:
                    if(z == z.p.left):#CASE 5
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = black #CASE 6
                    z.p.p.color = red
                    self.left_rotate(z.p.p)
        T.root.color = black#root must be colored black

    def RB_transplant(self,u,v):
        """Called by RB_delete
        This function swaps parent node u and child node v
        aka. Either u.left == v or u.right == v
        v.p == u
        """
        T = self
        if u.p == T.nil:#If u parent is nil
            T.root = v#v is now the root
        elif(u == u.p.left):#u is the left branch of u's parent
            u.p.left = v#replace u with v as left child of u's parent
        else:#u is the right branch of u's parent
            u.p.right = v#replace u with v as right child of u's parent
        v.p = u.p#set v to u

    def RB_delete(self,z):
        """This function deletes a node from the tree
        """
        T = self
        y = z
        y_original_color = y.color#retain original color of the node to delete
        if z.left == T.nil:#if left branch is a leaf
            x = z.right#set x to right branch
            self.RB_transplant(z,z.right)#switch node z with its right child
        elif(z.right == T.nil):
            x = z.left
            self.RB_transplant(z,z.left)
        else:
            y = self.tree_minimum(z.right)#sets y node to minimum node of tree
            y_original_color = y.color#sets y original color
            x = y.right#sets current node to t he right node of x
            if y.p == z:
                x.p = y
            else:
                self.RB_transplant(y,y.right)
                y.right = z.right
                y.right.p = y
            self.RB_transplant(z,y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == black:
            self.RB_delete_fixup(x)

    def RB_delete_fixup(self,x):
        T = self
        while (not (x == T.root)) and (x.color == black):#x is not the root node and the node color is not black
            if x == x.p.left:#x is a left child
                w = x.p.right#set w to x's sibling (right child of x's parent)
                if w.color == red:#If that node is red
                    w.color = black#color it black
                    x.p.color = red#set parent color black
                    self.left_rotate(x.p)#left rotate
                    w = x.p.right
                if w.left.color == black and w.right.color == black:
                    w.color = red
                    x = x.p
                else:
                    if(w.right.color == black):
                        w.left.color = black
                        w.color = red
                        self.right_rotate(w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = black
                    w.right.color = black
                    self.left_rotate(x.p)
                    x = T.root
            else: #x == x.p.right???
                #same as above with left and right switched
                w = x.p.left
                if w.color == red:
                    w.color = black
                    x.p.color = red
                    self.right_rotate(x.p)
                    w = x.p.left
                if w.right.color == black and w.left.color == black:
                    w.color = red
                    x = x.p
                else:
                    if(w.left.color == black):
                        w.right.color = black
                        w.color = red
                        self.left_rotate(w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = black
                    w.left.color = black
                    self.right_rotate(x.p)
                    x = T.root
        x.color = black

    def left_rotate(self,x):
        T = self
        y = x.right #Set y
        x.right = y.left # turn y's right subtree into x's left subtree
        if not y.left == T.nil:
            y.left.p = x
        y.p = x.p#relinks x's parent to y
        if x.p == T.nil:
            T.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x #put x on y's right
        x.p = y

    def right_rotate(self,x):
        T = self
        y = x.left #Set y
        x.left = y.right # turn y's right subtree into x's left subtree
        if not y.right == T.nil:
            y.right.p = x
        y.p = x.p #relinks x's parent to y
        if x.p == T.nil:
            T.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x #put x on y's right
        x.p = y

    def print_tree(self):
        """
        """
        T = self
        x = T.root

        #Get Max Height of Tree
        self.init_depth_first_search()
        maxHeight = max([len(self.myArray[i]) for i in np.arange(len(self.myArray))])

    def init_depth_first_search(self):
        """Initializes Depth First Search of Tree
        Updates myArray containing enumeration of all leaf to root branches
        Ex. [0,0,'x'] would be the root to leftmost branch
        """
        T=self
        x = T.root
        self.myArray = list()#will contain all boolean arrays
        branchEnum = list()
        depth_first_search(self,x,branchEnum)

    def find_node(self,key):
        """Finds Node with key
        Returns Node with key
        """
        T = self
        x = T.root
        cnt = 0
        while True:
            cnt += 1
            if x.key == key:
                return x
            elif(key < x.key):
                x = x.left
            else:#key > x.key
                x = x.right

            assert cnt < 10000,'find_node iterated too many times'

    def tree_minimum(self,x):
        """Iterates until at the very bottom left of tree given
        """
        while(x.left.key != None):
            x = x.left
        return x