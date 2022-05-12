from typing import Callable, Dict, Iterable, List
from typing_extensions import Self
from pinq.utils.decorators import module_not_imported

class IEnumerable(Iterable):
    def __new__(cls, *args, **kwargs):
        if cls is IEnumerable:
            raise TypeError(f"only children of '{cls.__name__}' may be instantiated")
        return object.__new__(cls)

    @module_not_imported("IEnumerable", "pinq.query.select")
    def Select(self, selector : Callable[..., object]) -> Self:
        pass

    @module_not_imported("IEnumerable", "pinq.query.where")
    def Where(self, predicate : Callable[..., bool]) -> Self:
        pass    
    
    @module_not_imported("IEnumerable", "pinq.query.prepend")
    def Prepend(self, element : object) -> Self:
        pass

    @module_not_imported("IEnumerable", "pinq.conversion")
    def ToList(self) -> List:
        pass
    
    @module_not_imported("IEnumerable", "pinq.conversion")
    def ToDictionary(self, key_selector : Callable[..., object], element_selector : Callable[..., object] = lambda element : element) -> Dict:
        pass