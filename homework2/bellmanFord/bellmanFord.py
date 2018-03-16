import numpy as np
import random


class bellmanFord(object):
    
    def __init_(self):
        pass

    def init_single_source(self,G,s):
        for i in range(1,abs(G.V)-1):
            for i in #for each edge (u,v) for all G.E
                self.relax(u,v,w)
        for #for each edge (u,v) for all G.E
            if v.d > u.d + w(u,v):
                return False
        return True