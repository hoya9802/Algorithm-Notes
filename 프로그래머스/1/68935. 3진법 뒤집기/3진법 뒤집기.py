def solution(n):
    n_3 = []
    while n>=1:
        n_3.append(n%3)
        n //= 3
    answer = 0
    for i, x in enumerate(n_3[::-1]):
        answer += (x * pow(3,i))
    return answer