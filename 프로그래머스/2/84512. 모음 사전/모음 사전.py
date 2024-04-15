from itertools import product

def solution(word):
    answer = []
    for i in range(1,6):
        ls = list(product(["A","E","I",'O','U'], repeat=i))
        for i in ls:
            answer.append(''.join(i))
    answer.sort()
    res = answer.index(word) + 1
        
    return res