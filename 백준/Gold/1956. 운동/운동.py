# 3 4
# 1 2 1
# 3 2 1
# 1 3 5
# 2 3 2

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            graph[s][e] = min(graph[s][e], graph[s][k] + graph[k][e])

res = INF
for i in range(1,n+1):
    for j in range(1, n+1):
        if INF > graph[i][j] > 0 and INF > graph[j][i] > 0:
            dist = graph[i][j] + graph[j][i]
            if res > dist:
                res = dist
if res == INF:
    print(-1)
else:
    print(res)