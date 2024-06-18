def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n%m)

def solution(w, h):
    return (w*h) - (w+h) + gcd(w,h)