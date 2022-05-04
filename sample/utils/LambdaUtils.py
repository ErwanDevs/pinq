from inspect import getargspec
from typing import Callable


class LambdaUtils(object):
    @staticmethod
    def get_number_of_arguments_taken(func: Callable[..., object]) -> int:
        return len(getargspec(func).args)
