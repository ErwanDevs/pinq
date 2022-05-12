import random

class Utils(object):
    @staticmethod
    def init_random_integer_list(seed : int = 0, size : int = 10, min = 1, max = 1000) -> list:
        random.seed(seed)
        return [random.randint(min,max) for _ in range(0,size+1)]

    @staticmethod
    def init_random_integer_dict(seed : int = 0, size : int = 10, min = 1, max = 1000) -> dict:
        random.seed(seed)
        return {i : random.randint(min,max) for i in range(0,size+1)}

    
        