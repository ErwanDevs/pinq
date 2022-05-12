import unittest
from pinq.enumerable_interface import IEnumerable
from pinq.enumerable import Enumerable
from pinq.utils.errors import ModuleNotImportedError
from tests.utils import Utils

class TestIEnumerable(unittest.TestCase):
    def test_initialization(self):
        with self.assertRaises(TypeError):
            IEnumerable()

    def test_function_call(self):  
        """
        This probably doesn't work because the select module was imported before here
        """   
        seed = 23
        size = 100
        enumerable = Enumerable(Utils.init_random_integer_list(seed, size))
        with self.assertRaises(AttributeError):
            enumerable.Select(lambda a : a)

if __name__ == '__main__':
    unittest.main()