import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1; graph[y][x] = 1

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            graph[s][e] = min(graph[s][e], graph[s][k] + graph[k][e])

min_val = INF
res = 0
for i in range(1, n+1):
    if min_val > sum(graph[i][1:]):
        min_val = sum(graph[i][1:])
        res = i
print(res)