from collections import Counter

def solution(topping):
    ans = 0
    forward = set()
    backward = Counter(topping)

    for i in topping:
        forward.add(i)
        backward[i] -= 1
        if backward[i] == 0:
            del backward[i]
        if len(forward) == len(backward.keys()):
            ans += 1
    return ans