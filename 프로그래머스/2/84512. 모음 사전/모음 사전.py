from itertools import product

def solution(word):
    answer = []
    for i in range(1,6):
        tmp = list(product(['A','E','I','O','U'], repeat=i))
        for j in tmp:
            answer.append(''.join(j))
    answer.sort()
    res = answer.index(word) + 1
        
    return res