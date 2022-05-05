import unittest
from pinq.enumerable import Enumerable
from tests.utils import Utils

class TestEnumerable(unittest.TestCase):
    def test_next(self):
        seed = 23
        size = 100
        enumerable = Enumerable(list(Utils.init_random_integer_list(seed, size)))
        try:
            enumerable.__next__()
        except Exception:
            self.fail("Enumerable next could not be called")

    def test_foreach(self):
        seed = 23
        size = 100
        enumerable = Enumerable(list(Utils.init_random_integer_list(seed, size)))
        try:
            (value for value in enumerable)
        except Exception:
            self.fail("Enumerable could not be enumerated in foreach")


    # test in foreach
    # test init
if __name__ == '__main__':
    unittest.main()