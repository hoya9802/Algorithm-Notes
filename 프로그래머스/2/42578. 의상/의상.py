# solve 2
from collections import Counter

def solution(clothes):
    tmp = 1
    answer = Counter([x for n, x in clothes])
    for i in answer.values():
        tmp *= (i+1)
    return tmp-1