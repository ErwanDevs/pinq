
from typing import Callable
from typing_extensions import Self
from pinq.enumerable import Enumerable
from pinq.enumerable_interface import IEnumerable
from pinq.utils.lambda_utils import LambdaUtils
from pinq.utils.decorators import extends


@extends(IEnumerable)
def Where(self, predicate : Callable[[object], bool]) -> IEnumerable:
    class WhereEnumerable(Enumerable):
            def __iter__(self):
                return (value for value in self.iterable if predicate(value))

    class WhereEnumerableWithIndex(Enumerable):
            def __iter__(self):
                return (value for value, index in enumerate(self.iterable) if predicate(value, index))

    match LambdaUtils.get_number_of_arguments_taken(predicate):
        case 1:
            return WhereEnumerable(self)
        case 2:
            return WhereEnumerableWithIndex(self)
        case _:
            raise ValueError("Comparison function must take one or two arguments")
