import sys
input = sys.stdin.readline

def dfs(x, n):
    visited[x] = n
    for i in graph[x]:
        if visited[i] == -1:
            dfs(i, n+1)
    return

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)

res = []
for i in range(1,n+1):
    visited = [-1] * (n+1)
    dfs(i,0)
    v = []
    res.append(visited[1:])

ans = 0
for i in range(n):
    h = res[i]; v = []
    for j in range(n):
        v.append(res[j][i])
    for x,y in zip(h,v):
        if x + y < 0:
            break
    else:
        ans += 1
print(ans)