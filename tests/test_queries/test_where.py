import unittest
from pinq.enumerable import Enumerable
from tests.utils import Utils
from pinq.query import where

class TestWhere(unittest.TestCase):
    def test_where(self):
        seed = 1
        size = 1000
        refList = Utils.init_random_integer_list(seed, size)
        condition = lambda a : a < 50            
        modifiedList = list(Enumerable(refList).Where(condition))
        for a in refList:
            if condition(a):
                self.assertTrue(a in modifiedList)
            else :
                self.assertFalse(a in modifiedList)

    def test_where_index(self):
        seed = 50
        size = 1000
        refList = Utils.init_random_integer_list(seed, size)
        condition = lambda number, index : number <= index * 10
        modifiedList = list(Enumerable(refList).Where(condition))
        for a, i in enumerate(refList):
            if condition(a, i):
                self.assertTrue(a in modifiedList)
            else :
                self.assertFalse(a in modifiedList)

if __name__ == '__main__':
    unittest.main()