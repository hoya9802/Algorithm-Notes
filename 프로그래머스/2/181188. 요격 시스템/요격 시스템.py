# solve 1

def solution(targets):
    targets.sort()
    res = bound = 0
    for target in targets:
        s, e = target
        if bound > s:
            bound = min(bound, e)
            continue
        bound = e
        res += 1
    return res