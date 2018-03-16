import numpy as np
import random

class graph(object):
    def __init__(self,V,E):
        self.V
        self.E


class bellmanFord(object):
    
    def __init_(self):
        pass

    def init_single_source(self,G,s):
        for i in range(0,G.V.shape[0]-1-1):#Iterate over all vertices-1 *Results in have indices from [0,3] for G.V.shape[0]=5 *because last one has already been gone over
            #V = G.V[G.V[i] != i]#recasts vertices to look at
            for j in range(0,G.E[i,:].shape[0]):#for each edge (u,v) for all G.E
                self.relax(u,v,w)
        for #for each edge (u,v) for all G.E
            if v.d > u.d + w(u,v):
                return False
        return True

    def relax(self,u,v,w):
        if v.d > u.d + w(u,v):#The distance from starting node s to current node v is longer than s to u + u to v
            v.d = u.d + w(u,v)#replace s to v with s to u + u to v
            v.pi = u #update v's predecessor attribute pi


    def check_negative_cycles(self,):
        #if v(s,n) < v(s,n-1):#for s to t, then negative cycles exist
            #then negative cycles return false
        pass
