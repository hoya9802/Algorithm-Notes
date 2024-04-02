def solution(n):
    answer = [True for _ in range(n+1)]
    for i in range(2, n+1):
        if answer[i] == True:
            j = 2
            while i * j <= n:
                answer[i*j] = False
                j += 1
    res = [x for x in range(2,n+1) if answer[x] == True]
    return len(res)