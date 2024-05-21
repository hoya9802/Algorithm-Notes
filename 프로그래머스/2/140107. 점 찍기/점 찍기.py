import math

def solution(k, d):
    ans = 0
    for i in range(d//k+1):
        ans += ((d**2-(k*i)**2)**(1/2))//k+1
    return ans