import math

def solution(k, d):
    ans = 0
    for i in range(0, d+1, k):
        ans += ((math.sqrt(d**2 - i**2))//k + 1)
    return int(ans)
        