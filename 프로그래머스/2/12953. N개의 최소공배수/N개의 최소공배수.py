import math
from functools import reduce

def solution(arr):
    return reduce(lambda x, y: x * y // math.gcd(x, y), arr)
    