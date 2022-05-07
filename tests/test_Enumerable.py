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
        empty = False
        while not empty:
            try:
                enumerable.__next__()
            except StopIteration:
                empty = True
        try:
            enumerable.__next__()
        except Exception:
            self.fail("Enumerable next could not be called while it should have been resetted")

    # foreach calls __iter__
    def test_foreach(self):
        seed = 23
        size = 100
        enumerable = Enumerable(list(Utils.init_random_integer_list(seed, size)))
        try:
            for _ in enumerable:
                continue
        except Exception:
            self.fail("Enumerable could not be enumerated in foreach")

        # enumerable should be reset
        enumerable.__next__()
        enumerable.__next__()
        for _ in enumerable:
            size -= 1
        # foreach iterate over a new enumerable with all elements, it should have the size of the original
        self.assertEqual(size, 0)


if __name__ == '__main__':
    unittest.main()