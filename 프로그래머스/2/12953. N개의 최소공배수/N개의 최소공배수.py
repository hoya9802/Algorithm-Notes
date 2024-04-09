# solve 2

def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n%m)

def solution(arr):
    answer = arr[0]
    for i in arr:
        tmp = answer * i // gcd(answer, i)
        answer = tmp
    return answer