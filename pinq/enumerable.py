from typing import Iterable
from typing_extensions import Self
from pinq.enumerable_interface import IEnumerable

from pinq.utils.iterable_utils import IterableUtils

# Note : Queries affect this after its current point, calling Enumerable.next() twice then using Enumerable.Select() will exclude the first two values
class Enumerable(IEnumerable):
    def __init__(self, iterable : Iterable):
        self.iterable = iterable

    def __iter__(self):
        return iter(self.iterable)


    


        