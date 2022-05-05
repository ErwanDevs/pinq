
from pinq.enumerable import Enumerable
from pinq.utils.decorators import extends 


@extends(Enumerable)
def ToList(self):
    new_list = list(self.generator) # generator to list empty the generator
    return new_list