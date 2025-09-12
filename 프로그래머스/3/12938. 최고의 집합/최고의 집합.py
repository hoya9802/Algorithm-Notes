def solution(n, s):
    if n > s:
        return [-1]
    ans = [int(s//n)] * n
    left = s%n
    for i in range(len(ans)-1, -1, -1):
        if left == 0:
            break
        ans[i] += 1
        left -= 1
    return ans
        
    