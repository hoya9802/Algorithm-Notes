import math
from itertools import combinations as cb

def is_prime_number(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    return len([sum(x) for x in list(cb(nums,3)) if is_prime_number(sum(x))==True])