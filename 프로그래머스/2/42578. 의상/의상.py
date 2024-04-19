# solve 3
from collections import Counter

def solution(clothes):
    answer = Counter([x for cl, x in clothes])
    temp = 1
    for i in answer.values():
        temp *= (i+1)
        
    return temp - 1