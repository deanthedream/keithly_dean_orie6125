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

    def test_runBA(self):
        from hybridSort import runBA



if __name__ == '__main__':
    unittest.main()