import numpy as np
import random

from findElement import findElement

fE = findElement()#create Instance
key = random.choice(fE.unordered)
sInd = fE.find_element(key)