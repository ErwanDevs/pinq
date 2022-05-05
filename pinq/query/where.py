
from typing import Callable
from typing_extensions import Self
from pinq import enumerable_interface
from pinq.utils.lambda_utils import LambdaUtils
from pinq.utils.decorators import extension


@extension(enumerable_interface)
def Where(self, comparison : Callable[[object], bool]) -> Self:
    match LambdaUtils.get_number_of_arguments_taken(comparison):
        case 1:
            self.generator = (value for value in self.generator if comparison(value))
        case 2:
            self.generator = (value for value, index in enumerate(self.generator) if comparison(value, index))
        case _:
            raise ValueError("Callable must take one or two arguments")
    return self