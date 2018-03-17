import numpy as np
import random

from bellmanFord import bellmanFord
from bellmanFord import graph

bF = bellmanFord()#create Instance

###############################################################
#Create Sample Directed Graph with No Negative Loops
VnoNegLoops = np.arange(0,5)
EnoNegLoops = np.array([    [0,1,1,0,0],
                            [0,0,1,0,0],
                            [0,0,0,1,0],
                            [0,1,0,0,1],
                            [1,0,0,0,0]])
#Parse out i to j connections taht exist nonzero edges
EnoNegList = [[i,j] for i in np.arange(len(EnoNegLoops[0,:])) for j in np.arange(len(EnoNegLoops[:,0])) if abs(EnoNegLoops[i,j]) > 0]
#Parse out weights
w = np.zeros(len(EnoNegList))
for i in np.arange(len(EnoNegList)):
    w[i] = EnoNegLoops[EnoNegList[i][0],EnoNegList[i][1]]
#no negative loops exist
GnoNegLoops = graph(VnoNegLoops,EnoNegList,w)  # Create graph 
LB, G = bF.bellman_ford(GnoNegLoops,0)

assert LB == True, 'Negative weight cycles were found'

################################################################
# Create Sample Directed Graph with Negative Loops
VNegLoops = np.arange(0,5)
ENegLoops = np.array([  [0,1,1,0,0],
                        [0,0,-1,0,0],
                        [0,0,0,-1,0],
                        [0,-1,0,0,1],
                        [1,0,0,0,0]])
#Parse out i to j connections that exist with nonzero weight
ENegList = [[i,j] for i in np.arange(len(ENegLoops[0,:])) for j in np.arange(len(ENegLoops[:,0])) if abs(ENegLoops[i,j]) > 0]
#Parse out weights
w = np.zeros(len(ENegList))
for i in np.arange(len(ENegList)):
    w[i] = ENegLoops[ENegList[i][0],ENegList[i][1]]
#1,2,3 is a negative loop
GNegLoops = graph(VNegLoops,ENegList,w)
LB, G = bF.bellman_ford(GNegLoops,0)
assert LB == False, 'Negative weight cycles were NOT found'

#If we were to randomly generate a graph, I would need to check...
#1. Each node has a vector leaving itself and going to another node (absolute value of row sum >= 1)
#2. Each node has a vector from another node to itself (absolute value of column sum >=1)
#3. Each node has a path from itself to every other node


