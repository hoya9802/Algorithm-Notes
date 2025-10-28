def solution(s):
    n = len(s); ans = 1
    for i in range(n):
        for j in range(i+1, n):
            tmp = s[i:j+1]
            if tmp == tmp[::-1] and len(tmp) > ans:
                ans = len(tmp)
    return ans
                