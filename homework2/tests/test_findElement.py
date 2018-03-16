import unittest
import sys
sys.path
sys.path.append('../findElement/.')
from findElement.findElement import findElement



import numpy as np
import random

class test_findElement(unittest.TestCase):
    

    def setUp(self):
        #Generate Tree Randomly for each case
        pass

    def test_find_element(self):
        """Randomly generate 30 trees from scratch to ensure all insert and fixup functions are tested
        """
        for i in np.arange(100):
            fE = findElement()
            key = random.choice(fE.unordered)
            ind = fE.find_element(key)

    def test_runFE(self):
        from findElement import runFE



if __name__ == '__main__':
    unittest.main()