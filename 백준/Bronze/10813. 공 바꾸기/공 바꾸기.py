import sys
input = sys.stdin.readline

n, m = map(int, input().split())

res = [x for x in range(0,n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    res[a], res[b] = res[b], res[a]

print(*res[1:])