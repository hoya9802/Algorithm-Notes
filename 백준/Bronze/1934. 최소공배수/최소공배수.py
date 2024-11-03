import sys
input = sys.stdin.readline

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n%m)

for _ in range(int(input())):
    a, b = map(int, input().split())
    tmp = gcd(a, b)
    print(tmp*(a//tmp)*(b//tmp))