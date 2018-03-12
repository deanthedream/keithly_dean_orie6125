#Red Black Tree Datastructure
#Authored by Dean Keithly

#import statements
import numpy as np


#Rule 1. Every Node is Red or Black
#Rule 2. The root is always black
#Rule 3. If a node is red, its children must be black
#Rule 4. Every path from the root to a leaf, or to a null child, 
#           must contain the same number of black nodes

#nil = 'nil'
black = False
red = True

# class Node(object):

#     def __init__(self,key):#,color,left=nil,right=nil,p=nil):
#         self.key = key #key
#         self.color = red#True for Red, Black for False
#         self.left = nil#right child of node key
#         self.right = nil#left child of node key
#         self.p = nil#parent of node key

#     # def __init__(self,key,color,left=nil,right=nil,p=nil):
#     #     self.key = key #key
#     #     self.color = False#True for Red, Black for False
#     #     self.left = left#right child of node key
#     #     self.right = right#left child of node key
#     #     self.p = p#parent of node key


class nil(object):
    def __init__(self):
        self.key = None
        self.color = False
        self.left = None
        self.right = None
        self.p = None

class Node(object):
    def __init__(self,key,nil_leaf):#,color,left=nil,right=nil,p=nil):
        self.key = key #key
        self.color = red#True for Red, Black for False
        self.left = nil_leaf#right child of node key
        self.right = nil_leaf#left child of node key
        self.p = nil_leaf#parent of node key

class Tree(object):
    def __init__(self,key,nil_leaf):
        """Tree must be initialized with a number
        """
        #Initialize Root
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
        '''Restores Red Black Correctness of tree
        '''
        T = self
        while z.p.color == red: #The color of the current node's parent is red
            if z.p == z.p.p.left:#current node's parent is left child of grandparent
                y = z.p.p.right#set y to right child of grandparent
                if y.color == red:#right child of grandparent is red
                    z.p.color = black#parent color is now black
                    y.color = black#right child of grandparent is black
                    z.p.p.color = red#grandparent is red
                    z = z.p.p#the current node is the grandparent
                else:#right child of grandparent is black
                    if(z == z.p.right):#The current node is an inside child of left branch
                        z = z.p#set current node to parent of current node
                        self.left_rotate(z)#rotate about parent node
                    z.p.color = black#color grandparent node to black
                    z.p.p.color = red#color current grandparent node to red
                    self.right_rotate(z.p.p)#
            else:#same as then clause above but with left and right swapped
                y = z.p.p.left
                if y.color == red:
                    z.p.color = black
                    y.color = black
                    z.p.p.color = red
                    z = z.p.p
                else:
                    if(z == z.p.left):
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = black
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
        '''This function deletes a node from the tree
        '''
        T = self
        y=z
        y_original_color = y.color#retain the original color of the node to delete
        if z.left == T.nil:#left branch is a leaf
            x = z.right#set x to right branch
            self.RB_transplant(z,z.right)#switch node z with its right child
        else:#right branch is a leaf
            y = self.tree_min(z.right)
            y_original_color = y.color
            x = y.right
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
        while (not (x == T.root)) and (x.color == black):
            if x == x.p.left:
                w = x.p.right
                if w.color == red:
                    w.color = black
                    x.p.color = red
                    self.left_rotate(x.p)
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
                w = x.p.right
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
        y = x.right
        x.right = y.left
        if not y.left == T.nil:
            y.left.p = x
        y.p = x.p
        if x.p == T.nil:
            T.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self,x):
        T = self
        y = x.left
        x.left = y.right
        if not y.right == T.nil:
            y.right.p = x
        y.p = x.p
        if x.p == T.nil:
            T.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

    # def print_tree(self):
    #     """
    #     """

    # def depth_first_search(self):
    #     T = self
    #     tree = list()
    #     x = T.root
    #     tree.append(x.left)
    #     tree.append(x.right)

    #     while np.any(not tree[i][-1] == None for i in np.arange(len(tree))):#While any elements of tree are not None
    #         ind = [i for i in np.arange(len(tree)) if not tree[i][-1] == None]#get index of branch without None
    #         branch = tree[ind]#boolean array not fully explored

    #         #Dive to last node in branch
    #         cnt = 0
    #         x = T.root
    #         for i in np.arange(len(branch)):
    #             if branch[i] == False:#left
    #                 x = x.left
    #             else: #branch[i] == True
    #                 x = x.right
    #         #x is now at the current unexplored node
    #         while True:
    #             #has left been explored
    #             branch.copy()
    #             indices = [i for i, s in enumerate(branch) if branch.copy().append(False) in s]
    #             if 

    #             #has right been explored
    #             if x.key == None:#If the branch is at a termination
    #                 branch.append('x')
    #                 break


    # def breadth_first_search(self,G,s):#G is the graph, s is the source node
    #     let Q be queue
    #     Q.enqueue(s) #insert s into queue until all its neighbor verticies are marked

    #     mark s as visited
    #     while (Q is not empty):
    #         #removing that vertex from queue, whose neighbor will be visited now

    #         v = Q.dequeue()

    #         #processing all neighbors of v
    #         for all neighbors w of v in Graph G
    #             if w is not visited
    #                 Q.enqueue(w)#Stores w in Q to further visit its neighbor
    #                 mark w as visited



    # def get_max_tree_height(self):
    #     """
    #     """
    #     T = self
    #     x = T.root
    #     cnt = 0#tree height counter

    #     # class queue(object):
    #     #     def __init__(self,T):
    #     #         self.p = T.nil
    #     #         self.left = T.nil
    #     #         self.right = T.nil
    #     #         self.toSearch

    #     sQueue = [hasattr(x,'left'),hasattr(x,'right')]
    #     while not([False,False] == sQueue):#Iterate until top queue indicates both branches of root have been fully explored
    #         kjashdfkljh


    #     def cntHeight(x,cnt,queue):
    #         return x
    #     val = cntHeight(T,cnt,)

    #     while len(queue.toSearch) > 0:#There is at least one leaf to search


    #     #Get max Val List
    #     maxValEncoding = list()
    #     while not x == T.nil:#While we haven't found a leaf
    #         x = x.right#Move down right branch
    #         maxValEncoding.append(1)#Append a 1 indicating right branch
    #         if x == T.nil:
    #             maxValEncoding.append('x')#Terminator




    #     #Now search Tree
    #     currentEncoding = list()
    #     while not currentEncoding == maxValEncoding:
    #         y = x
    #         if(not(x.left == T.nil)):#left node is not T.nil
    #             x = x.left#go down left Branch
    #             cnt += 1#height is higher
    #         elif(not(x.right == T.nil)):#the right node is not T.nil
    #             x = x.right#go down right branch
    #             cnt += 1#height is higher
    #         else:#The value is T.nil
