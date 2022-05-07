from typing import Iterable
from typing_extensions import Self
from pinq.enumerable_interface import IEnumerable

from pinq.utils.iterable_utils import IterableUtils

# Note : Queries affect this after its current point, calling Enumerable.next() twice then using Enumerable.Select() will exclude the first two values
class Enumerable(IEnumerable):
    def __init__(self, iterable : Iterable):
        self.generator = IterableUtils.generator_from_iterable(iterable)
        self.__tryNext()
        self.exhausted = []

    def __iter__(self):
        return self.__duplicate()

    def __duplicate(self) -> Self:
        temporary_list = list(self.generator)
        self.generator = IterableUtils.generator_from_iterable(temporary_list)
        temporary_list.extend(self.exhausted)
        return IterableUtils.generator_from_iterable(temporary_list)

    def __next__(self):
        if self.next == None:
            self.generator = IterableUtils.generator_from_iterable(self.exhausted)
            self.__tryNext()
            self.exhausted = []
            raise StopIteration
        self.exhausted.append(self.next)
        self.__tryNext()
        return self.exhausted[-1]

    def __tryNext(self):
        try:
            self.next = next(self.generator)
        except StopIteration:
            self.next = None
    


        