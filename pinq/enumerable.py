from typing import Iterable
from pinq.enumerable_interface import IEnumerable

from pinq.utils.iterable_utils import IterableUtils

class Enumerable(IEnumerable):
    def __init__(self, iterable : Iterable):
        self.generator = IterableUtils.generator_from_iterable(iterable)

    def __iter__(self):
        return iter(self.generator)

    def __next__(self):
        return next(self.generator)

    


        