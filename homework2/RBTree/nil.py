class nil(object):
    """nil must be created outside of Node object otherwise the nil created for each
    node will be different tree must be instantiated with a nil_leaf
    """
    def __init__(self):
        self.key = None
        self.color = False
        self.left = None
        self.right = None
        self.p = None