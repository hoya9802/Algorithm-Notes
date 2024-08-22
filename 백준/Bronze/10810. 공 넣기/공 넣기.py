n, m = map(int, input().split())

res = [0] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    for i in range(a,b+1):
        res[i] = c

print(*res[1:])