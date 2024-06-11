from itertools import product

def solution(word):
    res = []
    w = ['A','E','I','O','U']
    for i in range(1, len(w)+1):
        temp = list(product(w, repeat=i))
        res += [''.join(x) for x in temp]
    res.sort()
    return res.index(word) + 1
    