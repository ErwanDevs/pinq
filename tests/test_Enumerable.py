import random
import unittest
from weakref import ref
from sample.Enumerable import Enumerable

class TestEnumerable(unittest.TestCase):

    def __init_random_integer_list(self, seed : int = 0, size : int = 10) -> list:
        random.seed(seed)
        return list(random.randint(1,30) for _ in range(0,size))

    def test_select_data_modification(self):
        seed = 23
        size = 100
        refList = list(self.__init_random_integer_list(seed, size))
        modifiedList = Enumerable(refList).Select(lambda a : a+1)
        for a, b in zip(refList, modifiedList):
            self.assertEqual(a+1, b)

    def test__select_successive_queries(self):
        seed = 20
        size = 130
        refList = list(self.__init_random_integer_list(seed, size))
        modifiedList = Enumerable(refList).Select(lambda a : a+1).Select(lambda a : a -2)
        for a, b in zip(refList, modifiedList):
            self.assertEqual(a-1, b)

    def test_select_long_query(self):
        seed = 230
        size = 1000
        refList = list(self.__init_random_integer_list(seed, size))
        modifiedList = Enumerable(refList).Select(lambda a : a+1).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2).Select(lambda a : a -2).Select(lambda a : a +2)
        for a, b in zip(refList, modifiedList):
            self.assertEqual(a+1, b)

    def test_select_with_index(self):
        seed = 230
        size = 1000
        refList = list(self.__init_random_integer_list(seed, size))
        modifiedList = Enumerable(refList).Select(lambda a, i : a+i)
        i = 0
        for a, b in zip(refList, modifiedList):
            self.assertEqual(a+i, b)
            i+=1

    def test_where(self):
        seed = 1
        size = 1000
        refList = list(self.__init_random_integer_list(seed, size))
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
        refList = list(self.__init_random_integer_list(seed, size))
        condition = lambda number, index : number <= index * 10
        modifiedList = list(Enumerable(refList).Where(condition))
        for a, i in enumerate(refList):
            if condition(a, i):
                self.assertTrue(a in modifiedList)
            else :
                self.assertFalse(a in modifiedList)
if __name__ == '__main__':
    unittest.main()