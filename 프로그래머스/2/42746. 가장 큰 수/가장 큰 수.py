# solve 1
from functools import cmp_to_key

def compare(x, y):
    if x + y >= y + x:
        return -1
    else:
        return 1

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    res = ''.join(numbers)
    if res == '0' * len(res):
        return '0'
    else:
        return res