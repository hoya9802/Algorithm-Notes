import sys
input = sys.stdin.readline

def dfs(i, visited):
    for x in graph[i]:
        if not visited[x]:
            visited[x] = 1
            dfs(x, visited)
    return

n = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    m = map(int, input().split())
    for j in range(n):
        x = next(m)
        if x : graph[i].append(j)

for i in range(n):
    visited = [0] * n
    dfs(i, visited)
    print(' '.join(map(str, visited)))