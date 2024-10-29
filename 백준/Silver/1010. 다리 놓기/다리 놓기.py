import sys
input = sys.stdin.readline

def pm(x, n):
    total = 1
    for i in range(x, x-n, -1):
        total *= i
    return total

def cb(n, r):
    return pm(n,r) // pm(r,r)

for _ in range(int(input())):
    n, m = map(int, input().split())

    print(cb(m,n))