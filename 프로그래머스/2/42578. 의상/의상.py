# solve 6
from collections import Counter

def solution(clothes):
    ans = 1
    cc = Counter([k for x, k in clothes])
    for i in cc.values():
        ans *= (i+1)
    return ans-1
    
    