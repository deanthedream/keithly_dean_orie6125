import numpy as np

class Node(object):
    def __init__(self,num):
        self.num = num
        self.leftChild = None
        self.rightChild = None
        self.parent = None

    def insert(self,num):
        #inserts a new member into the tree

    def delete(self,num):
        #deletes node num

    def find(self,num):
        #returns the leftChild, rightChild, and parent of Node with num
