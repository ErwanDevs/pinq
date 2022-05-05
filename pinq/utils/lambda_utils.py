from inspect import getargspec
import inspect
from typing import Callable


class LambdaUtils(object):
    @staticmethod
    def get_number_of_arguments_taken(func: Callable[..., object]) -> int:
        return len(inspect.signature(func).parameters)
