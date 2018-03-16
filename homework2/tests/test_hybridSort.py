import unittest
import sys
sys.path
sys.path.append('../hybridSort/.')
from hybridSort.hybridSort import hybridSort

import numpy as np

class test_hybridSort(unittest.TestCase):
    

    def setUp(self):
        #Generate Tree Randomly for each case
        pass

    # def test_find_longest(self):
    #     """Randomly generate 30 trees from scratch to ensure all insert and fixup functions are tested
    #     """
    #     hS = hybridSort()
    #     firstInd, lastInd = hS.find_longest()

    def test_runHS(self):
        from hybridSort import runHS



if __name__ == '__main__':
    unittest.main()