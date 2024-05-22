import math

def solution(r1, r2):
    ans = 0
    for i in range(1, r2+1):
        if i < r1:
            ans += (math.floor(math.sqrt(r2**2-i**2))-math.ceil(math.sqrt(r1**2-i**2))+1)
        else:
            ans += (math.floor(math.sqrt(r2**2-i**2)) + 1)
    return ans * 4