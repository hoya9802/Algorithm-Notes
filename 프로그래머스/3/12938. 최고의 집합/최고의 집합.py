def solution(n, s):
    if n > s:
        return [-1]
    ans = [s//n] * n
    left = s%n
    
    p = len(ans)-1
    while left > 0:
        ans[p] += 1
        left -= 1
        p -= 1
    return ans