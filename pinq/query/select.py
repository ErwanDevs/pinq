import types
from typing import Callable
from typing_extensions import Self
from pinq.enumerable import Enumerable
from pinq.enumerable_interface import IEnumerable
from pinq.utils.lambda_utils import LambdaUtils
from pinq.utils.decorators import extends


@extends(IEnumerable)
def Select(self, selector : Callable[..., object]) -> IEnumerable:
    class SelectEnumerable(Enumerable):
            def __iter__(self):
                return (selector(value) for value in self.iterable)

    class SelectEnumerableWithIndex(Enumerable):
            def __iter__(self):
                return (selector(value, index) for value, index in enumerate(self.iterable))


    match LambdaUtils.get_number_of_arguments_taken(selector):
        case 1:
            return SelectEnumerable(self)
        case 2:
            return SelectEnumerableWithIndex(self)
        case _:
            raise ValueError("Given function must take one or two arguments")