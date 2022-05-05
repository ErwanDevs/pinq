
from typing import Iterable


class IterableUtils():
    @staticmethod
    def generator_from_iterable(iterable : Iterable):
        return (value for value in iterable)