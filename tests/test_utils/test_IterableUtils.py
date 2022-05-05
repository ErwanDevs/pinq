from collections.abc import Generator
import unittest
from pinq.utils.iterable_utils import IterableUtils
from tests.utils import Utils

class TestIterableUtils(unittest.TestCase):
    def test_empty_list_conversion(self):
        self.assertIsInstance(IterableUtils.generator_from_iterable([]), Generator)

    def test_list_conversion(self):
        seed = 23
        size = 100
        l = list(Utils.init_random_integer_list(seed, size))
        self.assertIsInstance(IterableUtils.generator_from_iterable(l), Generator)