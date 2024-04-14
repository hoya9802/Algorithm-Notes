# solve 1

from collections import Counter

def solution(clothes):
    ans = 1
    cc = Counter([name for x, name in clothes])
    for i in cc.values():
        ans = (i+1)*ans
        
    return ans-1