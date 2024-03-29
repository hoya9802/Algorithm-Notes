def solution(n):
    d = [0]*(n+1)
    d[0] = 0; d[1] = 1
    for i in range(2,n+1):
        if d[i] == 0:
            d[i] = d[i-1] + d[i-2]
        else:
            return d[i]
    answer = d[i] % 1234567
    return answer