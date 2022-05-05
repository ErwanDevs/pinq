from typing import Callable, Iterable
from typing_extensions import Self
from pinq.utils.decorators import module_not_imported

class IEnumerable(Iterable):
    def __new__(cls, *args, **kwargs):
        if cls is IEnumerable:
            raise TypeError(f"only children of '{cls.__name__}' may be instantiated")
        return object.__new__(cls)

    @module_not_imported("IEnumerable", "pinq.query.Select")
    def Select(self, func : Callable[..., object]) -> Self:
        pass