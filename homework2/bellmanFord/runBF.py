import numpy as np
import random

from bellmanFord import bellmanFord
from bellmanFord import graph

bF = bellmanFord()#create Instance

#Create Sample Directed Graph with No Negative Loops
VnoNegLoops = range(0,4)
EnoNegLoops = np.array([    [0,1,1,0,0],
                            [0,0,1,0,0],
                            [0,0,0,1,0],
                            [0,1,0,0,1],
                            [1,0,0,0,0]])
#no negative loops exist

#Create Sample Directed Graph with Negative Loops
VNegLoops = range(0,4)
ENegLoops = np.array([    [0,1,1,0,0],
                            [0,0,1,0,0],
                            [0,0,0,-1,0],
                            [0,-1,0,0,1],
                            [1,0,0,0,0]])

#1,2,3 is a negative loop

#Create Graph
GnoNegLoops = graph(VnoNegLoops,EnoNegLoops)
GNegLoops = graph(VNegLoops,ENegLoops)



#If we were to randomly generate a graph, I would need to check...
#1. Each node has a vector leaving itself and going to another node (absolute value of row sum >= 1)
#2. Each node has a vector from another node to itself (absolute value of column sum >=1)
#3. Each node has a path from itself to every other node


