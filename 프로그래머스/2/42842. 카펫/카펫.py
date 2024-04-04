import math

def solution(brown, yellow):
    answer = []
    n = brown+yellow
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            if (n//i - 2)*(i-2) == yellow:
                answer.append([n//i, i])
    return answer[-1]