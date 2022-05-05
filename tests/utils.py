import random

class Utils(object):
    @staticmethod
    def init_random_integer_list(seed : int = 0, size : int = 10) -> list:
        random.seed(seed)
        return list(random.randint(1,30) for _ in range(0,size))