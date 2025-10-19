def solution(s):
    res = 1
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            tmp = s[i:j+1]
            if tmp == tmp[::-1]:
                res = max(res, len(tmp))
    return res
            
                