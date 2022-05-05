
from typing import Callable
from typing_extensions import Self
from pinq import enumerable_interface
from pinq.utils.lambda_utils import LambdaUtils
from pinq.utils.decorators import extends


@extends(enumerable_interface)
def Select(self, func : Callable[..., object]) -> Self:
    match LambdaUtils.get_number_of_arguments_taken(func):
        case 1:
            self.generator = (func(value) for value in self.generator)
        case 2:
            self.generator = (func(value, index) for value, index in enumerate(self.generator))
        case _:
            raise ValueError("Callable must take one or two arguments")
    return self