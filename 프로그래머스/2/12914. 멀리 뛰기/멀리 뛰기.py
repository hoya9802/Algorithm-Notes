def solution(n):
    d = [0] * (n+1)
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        d[1] = 1; d[2] = 2
        for i in range(3, n+1):
            d[i] = d[i-2] + d[i-1]
    
    return d[n] % 1234567