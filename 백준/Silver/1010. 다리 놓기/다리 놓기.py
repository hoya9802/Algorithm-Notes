import sys
input = sys.stdin.readline

def cb(x, y):
    res = x
    for i in range(y-1):
        res *= (x-(i+1))
    return res

for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = cb(b,a) // cb(a, a)
    print(ans)
