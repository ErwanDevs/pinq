import unittest
from pinq.enumerable import Enumerable
from tests.utils import Utils

class TestEnumerable(unittest.TestCase):
    def test_initialization_with_different_iterable(self):
        seed = 9384
        size = 135
        dict = Utils.init_random_integer_dict(seed, size)
        enumerable = Enumerable(dict)
        for value, dict_tuple in zip(enumerable, dict.items()):
            self.assertEqual(value, dict_tuple[1])


    # foreach calls __iter__
    def test_foreach(self):
        seed = 23
        size = 100
        list = Utils.init_random_integer_list(seed, size)
        enumerable = Enumerable(list)
        try:
            # testing double enumeration
            for a, b in zip(enumerable, list):
                self.assertEqual(a, b)
            for a, b in zip(enumerable, list):
                self.assertEqual(a, b)
        except Exception:
            self.fail("Enumerable could not be enumerated in foreach")
        



if __name__ == '__main__':
    unittest.main()