from collections import Counter

def solution(weights):
    wc = Counter(weights)
    res = 0
    for i in wc.keys():
        if wc[i] > 1:
            res += (wc[i] * (wc[i] - 1)) // 2
        if wc[i*(3/2)] > 0:
            res += wc[i] * wc[i*(3/2)]
        if wc[i*(4/3)] > 0:
            res += wc[i] * wc[i*(4/3)]
        if wc[i*2] > 0:
            res += wc[i] * wc[2*i]
    return res