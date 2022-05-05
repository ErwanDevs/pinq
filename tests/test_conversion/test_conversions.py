import unittest
from pinq.enumerable import Enumerable
import pinq.conversion
from tests.utils import Utils


class TestConversionUtils(unittest.TestCase):
    def test_to_empty_list(self):
        enumerable = Enumerable([])
        self.assertIsInstance(enumerable.ToList(), list)

    def test_to_list(self):
        seed = 1
        size = 1000
        enumerable = Enumerable(Utils.init_random_integer_list(seed, size))
        self.assertIsInstance(enumerable.ToList(), list)


            
if __name__ == '__main__':
    unittest.main()