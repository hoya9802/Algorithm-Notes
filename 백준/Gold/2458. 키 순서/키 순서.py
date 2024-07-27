import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s][e] = 1

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            graph[s][e] = min(graph[s][e], graph[s][k] + graph[k][e])

res = 0
for i in range(1, n+1):
    h = graph[i][1:]; v = []
    for j in range(1, n+1):
        v.append(graph[j][i])
    for x,y in zip(h,v):
        if x + y >= INF * 2:
            break
    else:
        res += 1

print(res)