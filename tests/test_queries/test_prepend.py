from typing import Dict
import unittest
from pinq.enumerable import Enumerable
import pinq.query.prepend
from tests.utils import Utils


class TestPrepend(unittest.TestCase):
    def test_prepend(self):
        seed = 5098
        size = 1000
        refList = Utils.init_random_integer_list(seed, size)
        element = 9093
        enumerable = Enumerable(refList)
        new_enumerable = enumerable.Prepend(element)
        previous_value1 = None
        for value1, value2 in zip(enumerable, new_enumerable):
            if previous_value1:
                self.assertEqual(previous_value1, value2)
            else:
                self.assertEqual(value2, element)
            previous_value1 = value1

            
if __name__ == '__main__':
    unittest.main()