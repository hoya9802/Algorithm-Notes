import math

def solution(k, d):
    ans = 0
    for i in range(d//k+1):
        ans += (math.sqrt(d**2-(k*i)**2))//k+1
    return ans