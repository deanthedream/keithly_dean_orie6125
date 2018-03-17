import numpy as np
import random


NIL = None

class graph(object):

    def __init__(self,V,E,w):
        self.V = list()
        for i in np.arange(0,len(V)):
            self.V.append(vertice(V[i]))
        self.E = E#contains edge connections
        self.w = w#contains weights of edges

class vertice(object):

    def __init__(self,val):
        self.val = val
        self.d = np.inf
        self.pi = NIL

class bellmanFord(object):

    def __init_(self):
        pass

    def init_single_source(self,G,s):
        """
        Args:
            G - weighted directed Graph with vertices G.V and Weighted Edges G.E
            s - source index G.V[s] is the source Vertice
        """
        for i in np.arange(len(G.V)):
            G.V[i].d = np.inf#set all path from source to v to inf
            G.V[i].pi = NIL
        G.V[s].d = 0#The source vertice
        return G, s

    def bellman_ford(self, G,s):
        """
        Returns:
            cycleExists - boolean indicating whether a negative cycle is reachable from the source (True) or not (False)
        """
        G, s = self.init_single_source(G,s)
        w = G.w#w is the weighting vector

        array = np.arange(len(G.V))  # This is the full array of vertice indices
        #We need to iterate through all the nodes intelligently
        seen = list()
        tosee = list()
        tosee.append(s)#np.array([s])
        #for i in np.delete(array,s):  # Array does not include Node s
        while len(tosee) > 0:#There is at least one node to use as u
            i = tosee[0]
            # for each edge (u,v) for all G.E
            #for j in np.arange(len(G.E)):#Iterate through edges from u to next vertice. #np.arange(len(G.E)):
            #for j in [G.E[k] for k in np.arange(len(G.E[:])) if G.E[k][0] == i][0]:
            for j in [[G.E[k][1],k] for k in np.arange(len(G.E[:])) if G.E[k][0] == i]:
                #for []:
                #if G.E[j][0] == i:
                #uv = G.E[j]
                #u = uv[0]
                #v = uv[1]
                #if uv[0] == i:#I added this
                u = i
                v = j[0]
                #print(v)
                G = self.relax(G,u,v,w[j[1]])

                if not v in tosee and not v in seen:
                    tosee.append(v)#add to list of vertices to observe
                if not u in seen:
                    seen.append(u)#add u to array of vertices seen
                while u in tosee:
                    tosee.pop(0)
                    #tosee.pop(tosee.index(u))#remove seen vertice from list

            #print(tosee)
        # for each edge (u,v) for all G.E
        for i in np.arange(len(G.E)-1):
            uv = G.E[i]#uv is the from and to indice of edges
            u = uv[0]
            v = uv[1]
            print(' u=' + str(u)+' v='+str(v) + ' w=' + str(w[i]) + ' v.d=' + str(G.V[v].d) + ' u.d=' + str(G.V[u].d))

            if G.V[u].d > G.V[v].d + w[i]:#The addition of this u to v would decrease the current v.d
                if uv[1] == s or uv[0] == s:
                    return False, G#A negative cycle was found
        return True, G#A negative cycle was not found

    def relax(self,G,u,v,w):
        """Checks to see if the suggested path would be shorted
        G is the Graph
        u - starting vertice
        v - ending vertice
        w - weight for u to v
        """
        if G.V[v].d > G.V[u].d + w:  # The distance from starting node s to current node v is longer than s to u + u to v
            G.V[v].d = G.V[u].d + w  # replace s to v with s to u + u to v
            G.V[v].pi = G.V[u] # update v's predecessor attribute pi
        return G

