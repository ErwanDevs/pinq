import unittest
from pinq.enumerable import Enumerable
from tests.utils import Utils

class TestEnumerable(unittest.TestCase):
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