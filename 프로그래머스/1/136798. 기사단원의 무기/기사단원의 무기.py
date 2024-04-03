import math

def solution(n, limit, power):
    res = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(1, int(math.sqrt(i))+1):
            if i % j == 0:
                res[i] += 1
                if pow(j,2) != i:
                    res[i] += 1
        if res[i] > limit:
            res[i] = power
    return sum(res)