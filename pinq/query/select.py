
from typing import Callable
from typing_extensions import Self
from pinq.enumerable_interface import IEnumerable
from pinq.utils.lambda_utils import LambdaUtils
from pinq.utils.decorators import extends


@extends(IEnumerable)
def Select(self, selector : Callable[..., object]) -> IEnumerable:
    match LambdaUtils.get_number_of_arguments_taken(selector):
        case 1:
            self.generator = (selector(value) for value in self.generator)
        case 2:
            self.generator = (selector(value, index) for value, index in enumerate(self.generator))
        case _:
            raise ValueError("Given function must take one or two arguments")
    return self