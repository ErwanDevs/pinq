from typing import Iterable
from pinq.enumerable_interface import IEnumerable


# Note : Queries affect this after its current point, calling Enumerable.next() twice then using Enumerable.Select() will exclude the first two values
class Enumerable(IEnumerable):
    def __init__(self, iterable : Iterable):
        if hasattr( iterable, 'items' ):
            self.iterable = (value for key, value in iterable.items())
        else:
            self.iterable = iterable

    def __iter__(self):
        return iter(self.iterable)


    


        