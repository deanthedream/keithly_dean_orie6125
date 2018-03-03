#import statements
import numpy as np


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
        self.root.rb = False


    def insert(self,data):
        """
        """
        current = self.root
        while(True):
            if(data < current.data):
                if hasattr(current,'leftChild'):#Check that node has leftChild
                    current = current.leftChild
                else:#create that node
                    current.leftChild = self.Node(data)
                    #VALIDATE TREE COLOR
                    return
            if(data > current.data):
                if hasattr(current,'rightChild'):#Check that node has rightChild
                    current = current.rightChild
                else:#create that node
                    current.rightChild = self.Node(data)
                    #VALIDATE TREE COLOR
                    return
    # def insert(self,data):
    #     """
    #     """
    #     current = self.root
    #     while(True):
    #         if(data < current.data):#Update parent and leftChild
    #             parent = current#need to save an instance of the current node
    #             current = current.leftChild#the instance saving mechanism works.
    #             if(isinstance(current.data,type(None))):#create new Node
    #                 current = self.Node(data)
    #                 #parent.leftChild = data#hmmm  are these different instances or referencing the same thing... lets test this
    #                 return
    #         if(data > current.data):#Update parent and rightChild
    #             parent = current#need to save an instance of the current node
    #             current = current.rightChild
    #             if(isinstance(parent.rightChild.data,type(None))):
    #                 current = self.Node(data)
    #                 #parent.rightChild = data
    #                 return

        #NEED TO ADD COLORING CAPABILITIES

    def delete(self,data):
        """
        """
        #FIND NODE
        #CREATE SUBTREE
        #SAVE SUBTREE


# class Tree(object):
#     """
#     """
#     def __init__(self):
#         root = None#if this is the first None

#     def insert(self, data):
#         if(root == None):
#             root = Node()
#         else:
#         newNode = Node(data)


#         try:#check if root exists
#             root
#         except:
#             current = root
#             parent
#             while(True):
#                 parent = current
#                 #Check colors of parents and children
#                 if(current.rb == False and current.rightChild.rb == True and current.leftChild.rb == True):
#                     current.rb = True
#                     current.rightChild.rb = False
#                     current.leftChild.rb = False

#                 if(id < newNode.iData):#go Left
#                     current = current.leftChild
#                     if(current == None):
#                         parent.leftChild = newNode
#                         return
#                 else:#go right
#                     current = current.rightChild
#                     if(current == Null):
#                         parent.rightChild = newNode
#                         return
#         #END INSERT

#     def delete(self,id):

# class RBTree(object):
#     """A Red Black Tree Implementation
#     """

#     def __init__(self):
#         self.RBTree = list()#initialize RBTree

#     def addNumber(self, num):
#         """Adds number to red-black tree and modifies tree until a valid tree
#         """
#         #the number to be added must be unique


#         self.RBTree.append({'num':num,'color':'red','leftChild':None,'rightChild':None, 'parent':None})

#         #rootIndex = self.findRootIndex()#find root Index of tree
#         self.replaceNullTree(num)#we iteratively search the tree until we find a null tree (or phantom leaf) and can insert the element

#         #while(not self.tree_valid()):
#             #We rotate the tree until the tree is valid


#     def tree_valid(self):
#         """Check if Tree Is Valid

#         Return: True or False depending whether the tree is valid or not
#         """
#         #1 Every Node is Red or Black
#         color = np.ones((1,len(self.RBTree)),dtype=bool)#every color starts as True
#         for node in np.arange(len(self.RBTree)):
#             if not (self.RBTree[node]['color'] == 'red' or self.RBTree[node]['color'] == 'black'):
#                 color[node] = True #true here indicates there is no color assigned
#         assert sum(color) == 0, "All Nodes must have a color"

#         #2 The Root Node is Black


#         #3 No Red Node has a Red Child

#         #4 Every Root to Null Path pass through the same number of Black Nodes

#     def findRootIndex(self):
#         """Returns the index of the root of the red-black tree
#         """
#         for index in np.arange(len(self.RBTree)):
#             if self.RBTree[index]['parent'] == 'root':
#                 return index
#         print('Error root not found')

#     def findIndex(self,num):
#         """Returns index of RBTree entry with dict field 'num' of num
#         """
#         for index in np.arange(len(self.RBTree)):
#             if self.RBTree[index]['num'] == num:
#                 return index
#         print('Error num not found')

#     def replaceNullTree(self, num):
#         """Places the current num of the RBTree entry into the RBTree (determines what its parent is)
#         """
#         #index = findIndex(num)#this is the index of the current value
#         rootIndex = self.findRootIndex()
#         index = rootIndex
#         while((self.RBTree[index]['leftChild'] != None and self.RBTree[index]['num'] > num) or
#             (self.RBTree[index]['rightChild'] != None and self.RBTree[index]['num'] < num)):
#             if(self.RBTree[index]['num'] > num):#iteratively check index until at node with 1 empty child
#                 index = self.findIndex(self.RBTree[index]['rightChild'])#right children are inherently larger
#             else:#else num < current index num
#                 index = self.findIndex(self.RBTree[index]['leftChild'])
#         #We now have the index forming the parent of the new Node

#         #Populate the Child with the Parent Information
#         self.RBTree[index]['parent'] = num

#         #Populate Parent with Right Child/Left Child member
#         if self.RBTree[index]['num'] > num:#The new node is a leftChild
#             self.RBTree[index]['leftChild'] = num
#         else:#self.RBTree[index]['num'] > num#The new node is a rightChild
#             self.RBTree[index]['rightChild'] = num

#     #def rotateTree(self):
#         #Should be able to rotate trees with a more stable state


