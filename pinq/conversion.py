from typing import Callable, Dict, List
from pinq.enumerable import Enumerable
from pinq.utils.decorators import extends
from pinq.utils.iterable_utils import IterableUtils
from pinq.utils.lambda_utils import LambdaUtils 


@extends(Enumerable)
def ToList(self) -> List:
    return list(self.__iter__())

# Note: No equality comparer for dictionaries in Python = less work for me
@extends(Enumerable)
def ToDictionary(self, key_selector : Callable[..., object], element_selector : Callable[..., object] = lambda element : element) -> Dict:
    match LambdaUtils.get_number_of_arguments_taken(key_selector):
        case 1:
            arguments_taken_by_key_selector = 1
        case 2:
            arguments_taken_by_key_selector = 2
        case _:
            raise ValueError("Key selector function must take one or two arguments")    
    match LambdaUtils.get_number_of_arguments_taken(element_selector):
        case 1:
            arguments_taken_by_element_selector = 1
        case 2:
            arguments_taken_by_element_selector = 2
        case _:
            raise ValueError("Element selector function must take one or two arguments")
    # TODO : This is long, ugly, unreadable and unmaintanable, fix that 
    resulting_dictionary = {key_selector(*(*list(reversed(value_index_tuple))[0:arguments_taken_by_key_selector],)) : element_selector(*(*list(reversed(value_index_tuple))[0:arguments_taken_by_element_selector],)) for value_index_tuple in enumerate(self)}
    return resulting_dictionary