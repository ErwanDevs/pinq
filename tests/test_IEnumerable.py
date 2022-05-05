import unittest
from pinq.enumerable_interface import IEnumerable
from pinq.enumerable import Enumerable
from tests.utils import Utils

class TestIEnumerable(unittest.TestCase):
    def test_initialization(self):
        with self.assertRaises(TypeError):
            IEnumerable()

    def test_function_call(self):     
        seed = 23
        size = 100
        enumerable = Enumerable(list(Utils.init_random_integer_list(seed, size)))
        with self.assertRaises(AttributeError):
            enumerable.Select(lambda a : a)

if __name__ == '__main__':
    unittest.main()