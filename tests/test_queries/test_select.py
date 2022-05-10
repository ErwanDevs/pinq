import unittest
from tests.utils import Utils
from pinq.enumerable import Enumerable
import pinq.query

class TestSelect(unittest.TestCase):
    def test_select_data_modification(self):
        seed = 23
        size = 100
        refList = list(Utils.init_random_integer_list(seed, size))
        modifiedList = Enumerable(refList).Select(lambda a : a+1)
        for a, b in zip(refList, modifiedList):
            self.assertEqual(a+1, b)

    def test__select_successive_queries(self):
        seed = 20
        size = 130
        refList = list(Utils.init_random_integer_list(seed, size))
        enumerable = Enumerable(refList)
        modifiedList = enumerable.Select(lambda a : a+1).Select(lambda a : a -2)
        for a, b in zip(enumerable, modifiedList):
            self.assertEqual(a-1, b)

    def test_select_long_query(self):
        seed = 230
        size = 1000
        refList = list(Utils.init_random_integer_list(seed, size))
        modifiedList = Enumerable(refList).Select(lambda a : a+1).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2)
        for a, b in zip(refList, modifiedList):
            self.assertEqual(a+1, b)

    def test_select_with_index(self):
        seed = 3487
        size = 1000
        refList = list(Utils.init_random_integer_list(seed, size))
        modifiedList = Enumerable(refList).Select(lambda a, i : a+i)
        i = 0
        for a, b in zip(refList, modifiedList):
            self.assertEqual(a+i, b)
            i+=1

if __name__ == '__main__':
    unittest.main()