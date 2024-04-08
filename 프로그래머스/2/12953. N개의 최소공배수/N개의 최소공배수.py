def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n%m)

def solution(arr):
    tmp = arr[0]
    for i in arr:
        t = tmp * i // gcd(tmp, i)
        tmp = t
        
    return tmp