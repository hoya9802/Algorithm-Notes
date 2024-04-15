# solve 5

def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n%m)

def solution(arr):
    answer = arr[0]
    for i in arr:
        answer = answer * i // gcd(answer, i)
    return answer