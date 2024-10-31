import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n%m)

a, b = map(int, input().split())
d = gcd(a, b)

print((a//d)*(b//d)*d)