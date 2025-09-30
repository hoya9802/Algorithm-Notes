def solution(n, s):
    if n > s:
        return [-1]
    ll = s // n; lf = s % n
    res = [ll] * n
    idx = n-1
    while lf:
        res[idx] += 1
        lf -= 1; idx -= 1
    
    return res