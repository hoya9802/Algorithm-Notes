import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

parents = [x for x in range(n+1)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x

for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')

    else:
        union(a, b)
