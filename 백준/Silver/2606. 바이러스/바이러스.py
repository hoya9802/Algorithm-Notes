import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b); graph[b].append(a)

visited = [False] * (n+1)
res = 0
def dfs(start, visited):
    global res
    visited[start] = True
    res += 1
    for i in graph[start]:
        if not visited[i]:
            dfs(i, visited)
dfs(1, visited)
print(res-1)