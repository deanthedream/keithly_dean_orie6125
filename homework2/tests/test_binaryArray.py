import unittest
import hmwk2PATHS
from binaryArray.binaryArray import binaryArray
from binaryArray import runBA
hmwk2PATHS


class test_binaryArray(unittest.TestCase):

    def setUp(self):
        # Generate Tree Randomly for each case
        pass

    def test_find_longest(self):
        """Randomly generate 30 trees from scratch to ensure all insert and fixup functions are tested
        """
        bA = binaryArray()
        firstInd, lastInd = bA.find_longest()

    def test_runBA(self):
        runBA


if __name__ == '__main__':
    unittest.main()
