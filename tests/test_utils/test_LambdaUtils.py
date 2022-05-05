import unittest

from pinq.utils.lambda_utils import LambdaUtils

class TestLambdaUtils(unittest.TestCase):
    def test_get_number_of_arguments_taken(self):
        # 0 argument
        func = lambda : None
        self.assertEqual(LambdaUtils.get_number_of_arguments_taken(func), 0)
        # 2 arguments
        func = lambda a, b : None
        self.assertEqual(LambdaUtils.get_number_of_arguments_taken(func), 2)
        # more arguments than the number of taken argument
        func = lambda a, b, c : None
        self.assertEqual(LambdaUtils.get_number_of_arguments_taken(func), 3)
        # n arguments than the number of taken argument
        func = lambda *args : None
        self.assertEqual(LambdaUtils.get_number_of_arguments_taken(func), 1)

            
if __name__ == '__main__':
    unittest.main()