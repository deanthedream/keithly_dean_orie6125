import unittest
import sys
sys.path
sys.path.append('../binaryArray/.')
from binaryArray.binaryArray import binaryArray

import numpy as np

class test_binaryArray(unittest.TestCase):
    

    def setUp(self):
        #Generate Tree Randomly for each case
        pass

    def test_find_longest(self):
        """Randomly generate 30 trees from scratch to ensure all insert and fixup functions are tested
        """
        bA = binaryArray()
        firstInd, lastInd = bA.find_longest()

    def test_runBA(self):
        from binaryArray import runBA



if __name__ == '__main__':
    unittest.main()