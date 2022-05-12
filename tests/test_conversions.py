from typing import Dict
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

    # creating 2 lists should create 2 identical list
    def test_generator_reset_after_conversion(self):
        seed = 90
        size = 3400
        enumerable = Enumerable(Utils.init_random_integer_list(seed, size))
        list1 = enumerable.ToList()
        list2 = enumerable.ToList()
        self.assertListEqual(list1, list2)

    def test_bad_key_selector(self):
        seed = 24829
        size = 100
        enumerable = Enumerable(Utils.init_random_integer_list(seed, size))
        # Not enough arguments taken
        with self.assertRaises(ValueError):
            enumerable.ToDictionary(lambda : None)
        # Too many arguments_taken
        with self.assertRaises(ValueError):
            enumerable.ToDictionary(lambda a, b, c : None)

    def test_bad_element_selector(self):
        seed = 24829
        size = 100
        enumerable = Enumerable(Utils.init_random_integer_list(seed, size))
        # Not enough arguments taken
        with self.assertRaises(ValueError):
            enumerable.ToDictionary(lambda a : a, lambda : None)
        # Too many arguments_taken
        with self.assertRaises(ValueError):
            enumerable.ToDictionary(lambda a : a, lambda a, b, c : None)

    def test_to_empty_dictionary(self):
        enumerable = Enumerable([])
        self.assertIsInstance(enumerable.ToDictionary(lambda a : a), Dict)

    def test_no_element_selector(self):
        seed = 4897
        size = 987
        enumerable = Enumerable(Utils.init_random_integer_list(seed, size))
        # Without index (will delete element)
        key_selector = lambda a : a + 2
        resulting_dictionary = enumerable.ToDictionary(key_selector)
        self.assertIsInstance(resulting_dictionary, Dict)
        # Assert every key is here, assert the enumerable is reset as well
        for value in enumerable:
            self.assertIn((value+2, value), resulting_dictionary.items())
        # With index
        key_selector = lambda value, index : value+index
        resulting_dictionary = enumerable.ToDictionary(key_selector)
        self.assertIsInstance(resulting_dictionary, Dict)
        # Assert every key is here, assert the enumerable is reset as well
        for value, index in enumerate(enumerable):
            self.assertIn(value+index, resulting_dictionary)

    def test_with_element_selector(self):
        seed = 4897
        size = 987
        enumerable = Enumerable(Utils.init_random_integer_list(seed, size))
        # Without index (will delete element)
        key_selector = lambda a : a
        element_selector = lambda value : value
        resulting_dictionary = enumerable.ToDictionary(key_selector, element_selector)
        self.assertIsInstance(resulting_dictionary, Dict)
        # Assert every key is here, assert the enumerable is reset as well
        for value in enumerable:
            self.assertIn(value, resulting_dictionary)
        # With index
        key_selector = lambda a : a
        element_selector = lambda value, index : value + index
        resulting_dictionary = enumerable.ToDictionary(key_selector, element_selector)
        self.assertIsInstance(resulting_dictionary, Dict)
        # Assert every key is here, assert the enumerable is reset as well
        for value, index in enumerate(enumerable):
            self.assertIn(index, resulting_dictionary)
        # Without index for key selector (will delete element)
        key_selector = lambda value, index : value + index
        element_selector = lambda value : value
        resulting_dictionary = enumerable.ToDictionary(key_selector, element_selector)
        self.assertIsInstance(resulting_dictionary, Dict)
        # Assert every key is here, assert the enumerable is reset as well
        for value, index in enumerate(enumerable):
            self.assertIn(value+index, resulting_dictionary)
        # With index
        key_selector = lambda a, index : a + index
        element_selector = lambda value, index : value + index
        resulting_dictionary = enumerable.ToDictionary(key_selector, element_selector)
        self.assertIsInstance(resulting_dictionary, Dict)
        # Assert every key is here, assert the enumerable is reset as well
        for value, index in enumerate(enumerable):
            self.assertIn(value+index, resulting_dictionary)

    # normal dictionary = no problem -> assert each key is there and each element too
    # normal dictionary with element selector = no problem -> assert each key is there and each element is correct
    # Test with or without index 



            
if __name__ == '__main__':
    unittest.main()