# solve 1
from collections import Counter

def solution(clothes):
    ans = 1
    clo = Counter([n for x, n in clothes])
    
    for i in clo.values():
        ans = (i+1)*ans
    
    return ans - 1