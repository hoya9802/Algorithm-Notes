import math

def solution(r1, r2):
    res = 0
    for i in range(1, r2+1):
        if i < r1:
            res += (math.floor(math.sqrt(r2**2-i**2)) - math.ceil(math.sqrt(r1**2-i**2))+1)
        else:
            res += (math.floor(math.sqrt(r2**2-i**2))+1)
    return res * 4