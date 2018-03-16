import unittest
import hmwk2PATHS
from findElement.findElement import findElement
from findElement import runFE
import random
import numpy as np
hmwk2PATHS


class test_findElement(unittest.TestCase):

    def setUp(self):  # Generate Tree Randomly for each case
        pass

    def test_find_element(self):
        """Randomly generate 30 trees from scratch to ensure all insert and fixup functions are tested
        """
        for i in np.arange(100):
            fE = findElement()
            key = random.choice(fE.unordered)
            ind = fE.find_element(key)
        assert type(ind), 'asdf'

    def test_runFE(self):
        runFE


if __name__ == '__main__':
    unittest.main()
