from collections.abc import Generator, Callable
from inspect import signature
from typing import Iterable, Iterator
from typing_extensions import Self

from sample.utils.LambdaUtils import LambdaUtils

class Enumerable(Iterator):
    def __init__(self, iterable : Iterable):
        self.generator = (i for i in iterable)

    def __iter__(self):
        return iter(self.generator)

    def __next__(self):
        return next(self.generator)


    def Select(self, func : Callable[..., object]) -> Self:
        match LambdaUtils.get_number_of_arguments_taken(func):
            case 1:
                self.generator = (func(value) for value in self.generator)
            case 2:
                self.generator = (func(value, index) for value, index in enumerate(self.generator))
            case _:
                raise ValueError("Callable must take one or two arguments")
        return self

    def Where(self, comparison : Callable[[object], bool]) -> Self:
        match LambdaUtils.get_number_of_arguments_taken(comparison):
            case 1:
                self.generator = (value for value in self.generator if comparison(value))
            case 2:
                self.generator = (value for value, index in enumerate(self.generator) if comparison(value, index))
            case _:
                raise ValueError("Callable must take one or two arguments")
        return self


        