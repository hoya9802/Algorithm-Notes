def solution(n, s):
    if s//n == 0:
        return [-1]
    res = [s//n] * n
    
    count = int(s%n)
    for i in range(len(res)-1,-1,-1):
        if not count:
            break
        res[i] += 1
        count -= 1
        
    return res