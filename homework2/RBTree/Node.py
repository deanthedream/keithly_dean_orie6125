black = False
red = True

class Node(object):
    def __init__(self,key,nil_leaf):#,color,left=nil,right=nil,p=nil):
        self.key = key #key
        self.color = red#True for Red, Black for False
        self.left = nil_leaf#right child of node key
        self.right = nil_leaf#left child of node key
        self.p = nil_leaf#parent of node key