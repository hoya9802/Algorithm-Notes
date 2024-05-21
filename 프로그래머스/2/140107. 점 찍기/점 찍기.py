import math

def solution(k, d):
    ans = 0
    for i in range(math.ceil(d/k)+1):
        ans += (math.sqrt(d**2-(k*i)**2))//k+1
    return ans

from math import sqrt

def solution(k, d):
    answer = 0
    summ = 0

    for y in range(0, d + 1, k):
        x = d ** 2 - y ** 2
        cnt = sqrt(x) // k + 1
        summ += cnt

    return summ