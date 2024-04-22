# solve 4
from collections import Counter

def solution(clothes):
    answer = 1
    cnt = Counter([x for n, x in clothes])
    for i in cnt.values():
        answer *= (i + 1)
    return answer - 1