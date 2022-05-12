from typing import Callable
from typing_extensions import Self
from pinq.enumerable import Enumerable
from pinq.enumerable_interface import IEnumerable
from pinq.utils.lambda_utils import LambdaUtils
from pinq.utils.decorators import extends

@extends(IEnumerable)
def Prepend(self, element : object) -> IEnumerable:
    enumerable = Enumerable(self.iterable.copy())
    enumerable.iterable.insert(0, element)
    return enumerable