import math
from itertools import permutations as pm

def find_prime(x):
    if x == 1 or x == 0:
        return False
    else:
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True

def solution(numbers):
    res = set(); ans = 0
    for i in range(len(numbers)):
        for j in list(pm(numbers,i+1)):
            tmp = ''.join(j)
            res.add(int(tmp))
    for i in res:
        if find_prime(i) == True:
            ans += 1
    return ans