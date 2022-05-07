
from typing import Callable
from typing_extensions import Self
from pinq.enumerable_interface import IEnumerable
from pinq.utils.lambda_utils import LambdaUtils
from pinq.utils.decorators import extension


@extension(IEnumerable)
def Where(self, predicate : Callable[[object], bool]) -> IEnumerable:
    match LambdaUtils.get_number_of_arguments_taken(predicate):
        case 1:
            self.generator = (value for value in self.generator if predicate(value))
        case 2:
            self.generator = (value for value, index in enumerate(self.generator) if predicate(value, index))
        case _:
            raise ValueError("Comparison function must take one or two arguments")
    return self