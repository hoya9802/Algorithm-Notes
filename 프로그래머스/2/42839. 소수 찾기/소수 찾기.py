import math
from itertools import permutations as pm

def check_prime(x):
    ans = 0
    n = max(x)
    check = [True] * (n+1)
    check[0], check[1] = False, False
    for i in range(2, int(math.sqrt(n))+1):
        if check[i] == True:
            j = 2
            while i * j <= n:
                check[i*j] = False
                j += 1
    for i in x:
        if check[i] == True:
            ans += 1
    return ans

def solution(numbers):
    res = set(); ans = 0
    for i in range(len(numbers)):
        for j in list(pm(numbers,i+1)):
            tmp = ''.join(j)
            res.add(int(tmp))
    ans = check_prime(res)
    return ans