from typing import Callable
from typing_extensions import Self
from pinq.enumerable import Enumerable
from pinq.enumerable_interface import IEnumerable
from pinq.utils.lambda_utils import LambdaUtils
from pinq.utils.decorators import extends


@extends(IEnumerable)
def Select(self, selector : Callable[..., object]) -> IEnumerable:
    match LambdaUtils.get_number_of_arguments_taken(selector):
        case 1:
            select_iteration = lambda : (selector(value) for value in self)
        case 2:
            select_iteration = lambda : (selector(value, index) for value, index in enumerate(self))
        case _:
            raise ValueError("Given function must take one or two arguments")
    enumerable = Enumerable(self)
    enumerable.__iter__ = select_iteration
    return enumerable