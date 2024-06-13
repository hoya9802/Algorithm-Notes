import sys
from collections import deque
input = sys.stdin.readline

n, e, s = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b); graph[b].append(a)
graph = [sorted(x) for x in graph]
visited = [False] * (n+1)
def dfs(v):
    print(v, end=" ")
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
dfs(s)
print()

def bfs(v):
    visited = [False] * (n+1)
    q = deque([v])
    while q:
        now = q.popleft()
        if not visited[now]:
            print(now, end= " ")
            visited[now] = True
            for j in graph[now]:
                q.append(j)
bfs(s)