import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * (n)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b); graph[b].append(a)

def dfs(s, depth):
    visited[s] = True

    if depth == 5:
        print(1)
        exit()
        return
    
    for i in graph[s]:
        if not visited[i]:
            dfs(i, depth+1)
            visited[i] = False

for i in range(n):
    dfs(i, 1)
    visited[i] = False

print(0)