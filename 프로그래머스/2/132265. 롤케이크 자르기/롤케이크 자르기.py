from collections import Counter

def solution(topping):
    tc = Counter(topping)
    forward = set()
    res = 0
    for t in topping:
        forward.add(t)
        tc[t] -= 1
        if tc[t] == 0:
            del tc[t]
        if len(forward) == len(tc):
            res += 1
    return res