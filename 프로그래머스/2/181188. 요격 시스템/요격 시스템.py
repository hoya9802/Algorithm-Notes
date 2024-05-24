def solution(targets):
    ans = 0; bound = 0
    for target in sorted(targets):
        s, e = target
        if bound > s:
            bound = min(bound, e)
        else:
            bound = e
            ans += 1
    return ans